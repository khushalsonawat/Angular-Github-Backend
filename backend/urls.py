from django.contrib import admin
from django.urls import path, include
from github_user.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path('api/', include("github_user.urls")),
    path('api/', include("user_repository.urls")),
]
