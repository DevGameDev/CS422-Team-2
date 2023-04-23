from django.shortcuts import render
from django.views.generic import TemplateView


class UploadPageView(TemplateView):
    template_name = "upload/upload.html"

