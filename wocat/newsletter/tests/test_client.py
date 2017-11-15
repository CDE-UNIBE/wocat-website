from unittest.mock import Mock

from django.test import override_settings
import pytest

from wocat.newsletter.client import active_sync_only, newsletter_client


class TestNewsletterClient:
    """
    Test core functionality of MailChimp client wrapper. 
    """
    @pytest.fixture
    def user(self):
        return Mock(
            is_active=True,
            newsletter=True,
            email='foo@bar.com'
        )

    @override_settings(NEWSLETTER_IS_ACTIVE_SYNC=False)
    def test_wrapper_no_sync(self):
        func = Mock()
        active_sync_only(func)(self)
        assert not func.called

    @override_settings(NEWSLETTER_IS_ACTIVE_SYNC=True)
    def test_wrapper_active_sync(self):
        func = Mock()
        active_sync_only(func)(self)
        assert func.called

    def test_get_status_subscribed(self, user):
        assert newsletter_client.get_status(user=user) == 'subscribed'

    def test_get_status_invalid_mail(self, user):
        user.email = 'invalid'
        assert newsletter_client.get_status(user=user) == 'unsubscribed'

    def test_get_status_unsubscribed(self, user):
        user.newsletter = False
        assert newsletter_client.get_status(user=user) == 'unsubscribed'

    def test_get_status_inactive(self, user):
        user.is_active = False
        assert newsletter_client.get_status(user=user) == 'unsubscribed'
