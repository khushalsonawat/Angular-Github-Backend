from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
import requests


def home(request):
    return render(request, 'home.html')


class SendUserDataView(RetrieveAPIView):

    def get(self, request, username):
        url = "https://api.github.com/users/{}".format(username)
        response = requests.get(url)
        json_response = response.json()
        if response.status_code == 200:
            twitter_username = json_response["twitter_username"]
            email = json_response["email"]
            blog = json_response["blog"]
            data = {
                "username": username,
                "name": json_response["name"],
                "profile_url": json_response["html_url"],
                "bio": json_response["bio"],
                "avatar": json_response["avatar_url"],
                "location": json_response["location"],
            }
            if twitter_username:
                data["twitter_username"] = twitter_username
            if email:
                data["email"] = email
            if blog:
                data["blog"] = blog

            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response(json_response, status=response.status_code)
