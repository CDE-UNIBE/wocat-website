import base64

from django.db import models
from wagtail.wagtailcore.models import CollectionMember
from wagtail.wagtaildocs.models import AbstractDocument
from wagtail.wagtailsearch import index


# TODO: This field can be removed once https://github.com/torchbox/wagtail/pull/2992 is resolved.
class IndexingSearchField(index.SearchField):
    def get_value(self, obj):
        try:
            field = self.get_field(obj.__class__)
            value = field.value_from_object(obj)
            if isinstance(field, models.FileField):
                value = base64.b64encode(obj.file.file.read()).decode()
            if hasattr(field, 'get_searchable_content'):
                value = field.get_searchable_content(value)
            return value
        except models.fields.FieldDoesNotExist:
            value = getattr(obj, self.field_name, None)
            if hasattr(value, '__call__'):
                value = value()
            return value

class IndexedDocument(AbstractDocument):
    admin_form_fields = (
        'title',
        'file',
        'collection',
        'tags'
    )
    search_fields = CollectionMember.search_fields + [
        index.SearchField('title', partial_match=True, boost=10),
        IndexingSearchField('file'),  # TODO: set to index.SearchField
        index.RelatedFields('tags', [
            index.SearchField('name', partial_match=True, boost=10),
        ]),
        index.FilterField('uploaded_by_user'),
    ]
