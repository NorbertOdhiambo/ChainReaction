from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')


def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def test(request):
    return render(request, 'test.html')

def dashboard(request):
    form = HomePageForm()
    form2 = ServicePageForm()
    form3 = BlogPageForm()
    form4 = ServicesPageForm()
    form5 = ContactPageForm()

    if request.method == 'POST':
        form = HomePageForm(request.POST)
        form2 = ServicePageForm(request.POST)
        form3 = BlogPageForm(request.POST)
        form4 = ServicesPageForm(request.POST)
        form5 = ContactPageForm(request.POST)
        if form.is_valid():
            form.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()

    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5
    }
    return render(request, 'dashboard.html', context)
