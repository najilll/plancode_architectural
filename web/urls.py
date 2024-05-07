from django.urls import path
from . import views
app_name = 'web'
urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),
    path("about/",views.AboutView.as_view(), name="about"),
    path("contact/",views.ContactView.as_view(), name="contact"),
    path("portfolio/",views.PortfolioView.as_view(), name="portfolio"),
    path("blog/",views.BlogView.as_view(), name="blog"),
    path("blog-detail/",views.BlogdetailView.as_view(), name="blog-detail"),
]
