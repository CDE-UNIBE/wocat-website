from wagtail.wagtailcore.models import CollectionMember
from wagtail.wagtaildocs.models import AbstractDocument
from wagtail.wagtailsearch import index


class IndexedDocument(AbstractDocument):
    admin_form_fields = (
        'title',
        'file',
        'collection',
        'tags'
    )
    search_fields = CollectionMember.search_fields + [
        index.SearchField('title', partial_match=True, boost=10),
        index.SearchField('file'),
        index.RelatedFields('tags', [
            index.SearchField('name', partial_match=True, boost=10),
        ]),
        index.FilterField('uploaded_by_user'),
    ]
