from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.views import View
from wagtail.wagtailcore.models import Page, Collection
from wagtail.wagtaildocs.models import get_document_model
from django.utils.translation import ugettext_lazy as _

class DocumentUploadView(View):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        # get the related page
        page_pk = kwargs.get('page_pk')
        module_id = kwargs.get('module_id')
        upload_slug = kwargs.get('upload_slug')
        if file and page_pk and module_id and upload_slug:
            # create a document for this file
            document_cls = get_document_model()
            title = file
            collection_name = 'upload'
            try:
                collection = Collection.objects.get(name=collection_name)
            except Collection.DoesNotExist:
                root_collection = Collection.get_first_root_node()
                collection = root_collection.add_child(name=collection_name)
            document = document_cls.objects.create(title=title, file=file, collection=collection, uploaded_by_user=request.user)

            try:
                page = Page.objects.get(pk=page_pk).specific
            except Page.DoesNotExist:
                return

            # Add the document to the upload block.
            data = page.content.stream_data
            # ... manipulate data
            slug_found = False
            for item in data:
                type = item.get('type')
                if type == 'dsf_modules':
                    # data_index = data.index(item)
                    modules = item.get('value')
                    module_key = 'module_{0}'.format(module_id)
                    module = modules.get(module_key)
                    for block in module:
                        if block.get('type') == 'upload':
                            # module_index = module.index(block)
                            slug = block.get('value').get('upload_slug')
                            if slug and slugify(slug) == upload_slug:
                                documents = block.get('value').get('documents')
                                documents.append(document.pk)
                                slug_found = True
            if not slug_found:
                return HttpResponse(status=404)
            # save the new data
            import json
            data_json = json.dumps(data)
            page.content = data_json
            page.save()

            return HttpResponse('file uploaded')


class DocumentUploadDeleteView(View):
    def post(self, request, *args, **kwargs):
        # get the related document
        document_id = kwargs.get('document_id')
        if document_id:
            # get the document
            document_cls = get_document_model()
            try:
                document = document_cls.objects.get(id=document_id)
            except document_cls.DoesNotExist:
                return HttpResponse(status=404)
            # check if the user has permission
            if document.uploaded_by_user == request.user:
                # delete the document
                message = _('File "{document}" has been deleted.'.format(document=document))
                document.delete()
                messages.success(request, message)
            return redirect(self.request.GET.get('next', self.request.META.get('HTTP_REFERER', '/')))
