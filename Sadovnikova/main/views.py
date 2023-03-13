from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, template_name="main/layout.html")


def about_page(request):
    return render(request, template_name="main/home.html")
