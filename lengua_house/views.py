from django.shortcuts import render,
from django.http import HttpResponse

def home(request):
    return HttpResponse("home.html")

def about(request):
    return HttpResponse("about.html")

def bookings(request):
    return HttpResponse("bookings.html")

def admin_dashboard(request):
    return HttpResponse("admin_dashboard.html")
