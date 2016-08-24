from django.views.generic import TemplateView
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.backends import get_search_backend
from wagtail.wagtailsearch.models import Query

from wocat.glossary.models import Entry


class SearchView(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.search())
        return context

    def search(self):
        search_query = self.request.GET.get('query', None)
        if search_query:
            search_backend = get_search_backend()
            page_results = Page.objects.live().search(search_query)
            glossary_results = search_backend.search(search_query, Entry)
            # Log the query so Wagtail can suggest promoted results
            Query.get(search_query).add_hit()
            return {
                'search_query': search_query or '',
                'page_results': page_results,
                'glossary_results': glossary_results,
                'search_results': list(page_results) + list(glossary_results),
            }
        else:
            return {}
