from django.test import TestCase, RequestFactory
from .views import SendRepoDataView
import requests


class ValidUserTestCase(TestCase):
    def test_valid_user(self):
        valid_username = "ksonawat007"
        valid_url = "https://api.github.com/users/{}/repos".format(
            valid_username)
        request = RequestFactory().get("{}/repos".format(valid_username))
        view = SendRepoDataView()
        view.setup(request)
        view_response = view.get(request, valid_username)
        request_response = requests.get(valid_url)
        # print(view_response.data)
        self.assertEqual(len(view_response.data),
                         len(request_response.json()))

    def test_invalid_user(self):
        invalid_username = "kh2858"
        invalid_url = "https://api.github.com/users/{}/repos".format(
            invalid_username)
        request = RequestFactory().get("{}/".format(invalid_username))
        view = SendRepoDataView()
        view.setup(request)
        view_response = view.get(request, invalid_username)
        request_response = requests.get(invalid_url)
        self.assertEqual(
            view_response.data["message"], request_response.json()["message"])
