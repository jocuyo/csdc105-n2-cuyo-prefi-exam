# pages/views.py

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):  # added
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'connect.html'  # added

