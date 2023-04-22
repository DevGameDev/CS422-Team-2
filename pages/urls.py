from django.urls import path

from .views import HomePageView, ViewPageView, UploadPageView, DashboardPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("view/", ViewPageView.as_view(), name="view"),
    path("upload/", UploadPageView.as_view(), name="upload"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
]
