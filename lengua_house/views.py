from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from lengua_house.forms import BookingForm
from .models import AvailableSlot


# HTML pages
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def book(request):
    return render(request, "book_slot.html")


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


#  Tutor Login View
def tutor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:  # Only allow the tutor to log in
                login(request, user)
                return redirect('tutor_dashboard')  # Redirect to dashboard
            else:
                form.add_error(
                    None, "You are not authorized to access this page."
                    )
    else:
        form = AuthenticationForm()

    return render(request, 'tutor_login.html', {'form': form})


# Tutor Logout View
@login_required
def tutor_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page


# Tutor Dashboard View
@login_required
def tutor_dashboard(request):
    slots = AvailableSlot.objects.all()
    return render(request, 'admin_dashboard.html', {'slots': slots})


# Booking View
def book_slot(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.is_booked = True  # Mark slot as booked
            slot.save()
            return redirect('booking_success')  # Redirect to confirmation page
    else:
        form = BookingForm()

    available_slots = AvailableSlot.objects.filter(is_booked=False)
    return render(request, 'book_slot.html',
                  {'form': form, 
                   'available_slots': available_slots})
