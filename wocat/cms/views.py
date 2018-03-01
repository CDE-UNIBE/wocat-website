import json

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View, RedirectView
from wagtail.wagtailcore.models import Page, Collection
from wagtail.wagtaildocs.models import get_document_model


class AddLanguagePrefixRedirectView(RedirectView):
    """
    Redirect any unresolved URL not starting with a language prefix to /en/...
    """
    def get_redirect_url(self, *args, **kwargs):
        redirect_url = '/' + settings.LANGUAGES[0][0] + self.request.get_full_path()
        if not redirect_url.endswith('/'):
            redirect_url += '/'
        get_object_or_404(Page, url_path='/home' + redirect_url)
        return redirect_url


class DocumentUploadView(View):
    """
    Handle uploaded documents of DSF.
    """
    dsf_collection_name = 'DS-SLM Upload'

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        # get the related page
        page_pk = kwargs.get('page_pk')
        module_id = kwargs.get('module_id')

        # Get page
        try:
            page = Page.objects.get(pk=page_pk).specific
        except Page.DoesNotExist:
            return HttpResponse(status=404)

        # Check permissions
        if page.permissions_for_user(request.user).can_edit() is False:
            return HttpResponse(status=401)

        # Get or create collection
        try:
            collection = Collection.objects.get(name=self.dsf_collection_name)
        except Collection.DoesNotExist:
            root_collection = Collection.get_first_root_node()
            collection = root_collection.add_child(
                name=self.dsf_collection_name)

        # Add the document to the upload block. As there are multiple upload
        # blocks on the same page, the correct one needs to be found.
        data = page.content.stream_data
        document_location_found = False
        for item in data:
            if item.get('type') != 'dsf_modules':
                continue

            modules = item.get('value', {})
            module_key = 'module_{}'.format(module_id)
            for block in modules.get(module_key, []):
                if block.get('type') != 'upload':
                    continue

                module_name = modules.get('{}_title'.format(module_key))
                title = ' - '.join([page.title, module_name, str(file)])

                # Create document and add it to the list
                document_cls = get_document_model()
                document = document_cls.objects.create(
                    title=title, file=file, collection=collection,
                    uploaded_by_user=request.user)

                documents = block.get('value', {}).get('documents', [])
                documents.append(document.pk)
                document_location_found = True

        if not document_location_found:
            return HttpResponse(status=404)

        # Save the new data
        data_json = json.dumps(data)
        page.content = data_json
        page.save()

        return HttpResponse('file uploaded')


class DocumentUploadDeleteView(View):
    """
    Delete an uploaded document.
    """
    def post(self, request, *args, **kwargs):
        # Get the document
        document_id = kwargs.get('document_id')
        document_cls = get_document_model()
        try:
            document = document_cls.objects.get(id=document_id)
        except document_cls.DoesNotExist:
            return HttpResponse(status=404)
        # Check if the user has permission
        if document.uploaded_by_user == request.user:
            # Delete the document
            message = 'File "{document}" has been deleted.'.format(
                document=document)
            document.delete()
            messages.success(request, message)
        return redirect(self.request.GET.get(
            'next', self.request.META.get('HTTP_REFERER', '/')))
