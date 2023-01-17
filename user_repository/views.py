from rest_framework.response import Response
import requests
from rest_framework.generics import RetrieveAPIView
from .serializers import RepositorySerializer


class SendRepoDataView(RetrieveAPIView):
    queryset = []

    def get(self, request, username):
        url = "https://api.github.com/users/{}/repos".format(username)
        response = requests.get(url)
        json_response = response.json()
        if response.status_code == 200:
            data = []
            # print(json_response)
            for i in json_response:
                repo_data = {}
                repo_data = {
                    "title": i["name"],
                    "url": i["html_url"]
                }

                languages = requests.get(i["languages_url"]).json()
                repo_data["topics"] = list(languages.keys())

                if i["description"]:
                    repo_data["description"] = i["description"]
                else:
                    repo_data["description"] = ""

                data.append(repo_data)
            serialized_data = RepositorySerializer(data=data, many=True)
            data_to_be_sent = {}
            if serialized_data.is_valid():
                data_to_be_sent = serialized_data.data
            return Response(data_to_be_sent, status=response.status_code)

        else:
            return Response(json_response, status=response.status_code)
