from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
# required for database transactions, ref: simpleisbetterthancomplex
from django.db import transaction
from django import forms
# required for profile update, ref: simpleisbetterthancomplex
from django.contrib import messages
from .models import User
from .forms import UserForm, UserProfileForm, UserRegistrationForm


def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='/accounts/login')
def check_auth(request):
    return render(request, 'accounts/check.html')


def user_registration(request):
    # This is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request (binding data to the form):
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            # print(registration_form.cleaned_data)
            # Create new User
            user = User.objects.create_user(username=registration_form.cleaned_data['username'],
                                            password=registration_form.cleaned_data['password'],
                                            email=registration_form.cleaned_data['email'])
            # Send verification email
            # redirect to login page
            return redirect('/accounts/login')
        else:
            return render(request, 'accounts/user_registration.html', {'registration_form': registration_form})
    # if a GET (or any other method) we'll create a blank form
    else:
        registration_form = UserRegistrationForm()
        return render(request, 'accounts/user_registration.html', {'registration_form': registration_form})


# ref: simpleisbetterthancomplex
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
            return redirect('/accounts/profile')
        else:
            messages.error(request, 'Please correct the error above.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required(login_url='/accounts/login')
@user_passes_test(lambda u: u.is_staff)
def create_project(request):
    return HttpResponse("You can create project and you can create group")

