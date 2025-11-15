from django.shortcuts import render, redirect
from .forms import MembershipForm
from .models import GymMember
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
def home(request):
    return render(request, 'gym/home.html')


@user_passes_test(lambda u: u.is_staff)
def register_member(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MembershipForm()
    return render(request, 'gym/register.html', {'form': form})

@login_required
def dashboard(request):
    members = GymMember.objects.all()
    return render(request, 'gym/dashboard.html', {'members': members})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'gym/signup.html', {'form': form})