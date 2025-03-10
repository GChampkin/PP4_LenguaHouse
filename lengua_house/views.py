from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 

# HTML pages
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def bookings(request):
    return render(request, "bookings.html")

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

#Tutor Login View
def tutor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:  # Only allow the tutor to log in
                login(request, user)
                return redirect('dashboard')  # Redirect to admin dashboard
            else:
                form.add_error(None, "You are not authorized to access this page.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'admin_dashboard.html', {'form': form})

# Tutor Logout View
@login_required
def tutor_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page
