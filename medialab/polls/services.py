import requests

from django.conf import settings


class PollsService():
    def request(self, method, resource, params, jwt):
        return requests.request(
            method,
            settings.POLLS_URL + '{}'.format(resource),
            params=params,
            headers={'Authorization': 'Bearer {}'.format(jwt)},
        )