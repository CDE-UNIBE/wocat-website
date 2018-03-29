from unittest import mock

from django.core.management import call_command
from django.urls import reverse
import pytest


from wocat.api.views import MapSearchView


class TestMapAPI:
    """"
    Test responses for API endpoints in use for the map-search.
    """
    @pytest.fixture
    def projects(self):
        """
        Mocking all necessary wagtail-models is a pain, so use slow fixtures.
        """
        try:
            call_command('loaddata', 'wocat/api/tests/fixtures/projects.json', **{
                'verbosity': 0,
                'commit': False,
            })
        except Exception:
            raise

    @pytest.fixture
    def map_view(self, rf):
        view = MapSearchView()
        view.kwargs = {'filter': 'projects'}
        view.request = rf.get(reverse('map_search', kwargs={'filter': 'projects'}))
        return view

    @pytest.mark.django_db
    def test_project_search_all(self, projects, map_view):
        """
        All projects for active language must be on display without a filter.
        """
        search = map_view.get_projects()
        assert ['cascade', 'desire'], [page.title for page in search['pages']]

    @pytest.mark.django_db
    def test_project_filter_search(self, projects, map_view):
        """
        Only 'matching' projects for active language must be shown.
        """
        with mock.patch.object(MapSearchView, 'query_string', new_callable=mock.PropertyMock) as query:
            query.return_value = 'cascade'
            search = map_view.get_projects()
            assert 'cascade', [page.title for page in search['pages']]

    @pytest.mark.django_db
    def test_non_english_project(self, projects, map_view):
        """
        Without a 'filter', only projects with the currently active languages are shown.
        """
        with mock.patch('django.utils.translation.get_language_from_request') as get_lang:
            get_lang.return_value = 'fr'
            search = map_view.get_projects()
            assert 'fr - cascade', [page.title for page in search['pages']]

    @pytest.mark.django_db
    def test_non_english_filter(self, projects, map_view):
        """
        With a filter, non-tranlsated projects are included in the search.
        """
        with mock.patch('django.utils.translation.get_language_from_request') as get_lang:
            get_lang.return_value = 'fr'
            with mock.patch.object(MapSearchView, 'query_string', new_callable=mock.PropertyMock) as query:
                query.return_value = 'desire'
                search = map_view.get_projects()
                assert 'desire', [page.title for page in search['pages']]

