from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("store/", views.store, name="store"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("testimonial/", views.testimonial, name="testimonial"),
    
    path('admin/', admin.site.urls),
]
