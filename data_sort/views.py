from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "data_sort/home.html"


class ViewPageView(TemplateView):
    template_name = "data_sort/view.html"


class DashboardPageView(TemplateView):
    template_name = "data_sort/dashboard.html"

# Create your views here.
