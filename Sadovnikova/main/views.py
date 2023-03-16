from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, template_name="main/home.html", context={"title": "Home page"})


def about_page(request):
    return render(request, template_name="main/about.html", context={"title": "About me"})
