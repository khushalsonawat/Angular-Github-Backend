from django.urls import path
from .views import SendRepoDataView

urlpatterns = [
    path("<str:username>/repos/", SendRepoDataView.as_view())
]
