from django.urls import path

from .views import ViewPageView, HomePageView, DashboardPageView


urlpatterns = [
    path("view/", ViewPageView.as_view(), name="view"),
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
]