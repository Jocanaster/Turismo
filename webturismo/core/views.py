from django.shortcuts import render # type: ignore

def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def services(request):
    return render(request, "core/services.html")

def store(request):
    return render(request, "core/store.html")

def contact(request):
    return render(request, "core/contact.html")

def blog(request):
    return render(request, "core/blog.html")

def testimonial(request):
    return render(request, "core/testimonial.html")
