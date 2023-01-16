from django.urls import path
from .views import SendUserDataView

urlpatterns = [
    path('<str:username>/', SendUserDataView.as_view()),
]
