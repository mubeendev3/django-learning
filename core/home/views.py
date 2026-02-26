from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    people = [
        {"name": "Mubeen Mehmood", "age": 21},
        {"name": "Muhammad Mushahid", "age": 22},
        {"name": "Muhammad Arbaz", "age": 17},
        {"name": "Muhammad Saeed", "age": 24},
        {"name": "Hafiz Kamran", "age": 16},
    ]
    return render(request, 'index.html', {"people": people})

def success_page(request):
    return HttpResponse("<h1>Success page</h1>")

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')

def login_page(request):
    return render(request, 'login.html')