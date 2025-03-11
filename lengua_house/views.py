from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import TutorSchedule
from .forms import BookingForm


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
    booked_slots = TutorSchedule.objects.filter(is_booked=True)
    return render(request, "tutor_dashboard.html",
                  {"booked_slots": booked_slots})


# Booking View
def book_slot(request):
    available_slots = TutorSchedule.objects.filter(is_booked=False)

    if request.method == "POST":
        slot_id = request.POST.get("slot_id")
        slot = get_object_or_404(TutorSchedule, id=slot_id)
        form = BookingForm(request.POST, instance=slot)

        if form.is_valid():
            slot.is_booked = True  
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, "book_slot.html",
                  {"available_slots": available_slots})
