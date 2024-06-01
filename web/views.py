from django.http import JsonResponse
from django.shortcuts import render

from .models import Baner,Portfolio,Transformation,Employee,Testimonial,PortfolioCategory,Blog
from django.views.generic import TemplateView,DetailView,FormView
from .forms import ContactForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baner'] = Baner.objects.filter(is_active=True)
        context['portfolio'] = Portfolio.objects.filter(is_active=True,is_home=True)
        context['transformation'] = Transformation.objects.first()
        context['employees'] = Employee.objects.filter(is_active=True)
        context['testimonial'] = Testimonial.objects.filter(is_active=True)
        context['blogs'] = Blog.objects.filter(is_active=True,is_home=True)[:2]

        return context


class AboutView(TemplateView):
    template_name = "web/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(is_active=True)
        context['testimonial'] = Testimonial.objects.filter(is_active=True)

        return context


class ContactView(TemplateView):
    template_name = "web/contact.html"


class PortfolioView(TemplateView):
    template_name = "web/portfolio.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = Portfolio.objects.filter(is_active=True)
        context['category'] = PortfolioCategory.objects.filter(is_active=True)

        return context


class BlogView(TemplateView):
    template_name = "web/blog.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(is_active=True)
        return context


class BlogdetailView(DetailView):
    model = Blog
    template_name = "web/blog-details.html"


class Portfolio_DetailView(DetailView):
    model = Portfolio
    template_name = "web/post-details.html"

class ContactView(TemplateView,FormView):
    template_name = "web/contact.html"
    form_class = ContactForm

    def get(self, request):
        form = ContactForm()
        context = {
            "form": form,
        }
        return render(request, "web/contact.html", context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Our team will contact you soon !!",
                'redirect' :True
            }
            return JsonResponse(response_data)
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({"status": "false", "errors": errors}, status=400)