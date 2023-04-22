from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"
    

class ViewPageView(TemplateView):
    template_name = "pages/view.html"

class UploadPageView(TemplateView):
    template_name = "pages/upload.html"

class DashboardPageView(TemplateView):
    template_name = "pages/dashboard.html"
