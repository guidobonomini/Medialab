from unittest.mock import Mock

from django.test import TestCase
from django.conf import settings

from medialab.users.tests.factories import UserFactory
from medialab.polls.services import PollsService


class ServiceTestCase(TestCase):
    def test_get_to_service(self):
        user = UserFactory()
        MockService = Mock()
        params = {'foo': 'bar'}

        expected_headers = {'Authorization': 'Bearer {}'.format(user.get_jwt())}
        MockService.request.assert_called_once_with(
            'GET',
            settings.POLLS_URL,
            params=params,
            headers=expected_headers
        )