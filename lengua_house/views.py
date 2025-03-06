from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def bookings(request):
    return render(request, "bookings.html")

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")
