from django.shortcuts import render
from .models import Baner,Portfolio,Transformation,Employee,Testimonial
from django.views.generic import TemplateView,DetailView
# Create your views here.

class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baner'] = Baner.objects.filter(is_active=True)
        context['portfolio'] = Portfolio.objects.filter(is_active=True)
        context['transformation'] = Transformation.objects.first()
        context['employees'] = Employee.objects.filter(is_active=True)
        context['testimonial'] = Testimonial.objects.filter(is_active=True)

        return context


class AboutView(TemplateView):
    template_name = "web/about.html"