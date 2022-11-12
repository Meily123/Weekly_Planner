from django.shortcuts import render
from django.views.generic import TemplateView


class cobaTemplate(TemplateView):
    template_name = 'test.html'
