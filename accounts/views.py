from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# required for database transactions, ref: simpleisbetterthancomplex
from django.db import transaction
# required for profile update, ref: simpleisbetterthancomplex
from django.contrib import messages
from .forms import UserForm, UserProfileForm


def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='/accounts/login')
def check_auth(request):
    return render(request, 'accounts/check.html')


@login_required(login_url='/accounts/login')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('accounts:check')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })