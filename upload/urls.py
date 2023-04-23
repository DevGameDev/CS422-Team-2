from django.urls import path

from .views import UploadPageView

urlpatterns = [
    path("", UploadPageView.as_view(), name="upload"),
]
