from django.http import HttpResponse
from django.views import View
from wagtail.wagtailcore.models import Page, Collection
from wagtail.wagtaildocs.models import get_document_model


class DocumentUploadView(View):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        # get the related page
        page_pk = kwargs.get('page_pk')
        module_id = kwargs.get('module_id')
        if file and page_pk and module_id:
            # create a document for this file
            document_cls = get_document_model()
            title = file
            collection_name = 'upload'
            try:
                collection = Collection.objects.get(name=collection_name)
            except Collection.DoesNotExist:
                root_collection = Collection.get_first_root_node()
                collection = root_collection.add_child(name=collection_name)
            document = document_cls.objects.create(title=title, file=file, collection=collection)

            try:
                page = Page.objects.get(pk=page_pk).specific
            except Page.DoesNotExist:
                return

            # Add the document to the upload block.
            data = page.content.stream_data
            # ... manipulate data
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
                            documents = block.get('value').get('documents')
                            documents.append(document.pk)
            # save the new data
            import json
            data_json = json.dumps(data)
            page.content = data_json
            page.save()

            return HttpResponse('file uploaded')
