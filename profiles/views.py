from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.


def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})


def add_profile(request):
    profile_form = ProfileForm()
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    return render(request, 'profile.html', {'form': profile_form})
