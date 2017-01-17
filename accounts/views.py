from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
# required for database transactions, ref: simpleisbetterthancomplex
from django.db import transaction
from django import forms
# required for profile update, ref: simpleisbetterthancomplex
from django.contrib import messages
from .models import User
from .forms import UserForm, UserProfileForm, UserRegistrationForm, MyUsersForm


def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='/accounts/login')
def check_auth(request):
    return render(request, 'accounts/check.html')


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def user_registration(request):
    # This is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request (binding data to the form):
        registration_form = UserRegistrationForm(request.POST)
        my_user_form = MyUsersForm(request.POST)
        # Both forms have to be valid
        if registration_form.is_valid() and my_user_form.is_valid():
            # Create new User
            user = User.objects.create_user(username=registration_form.cleaned_data['username'],
                                            password=registration_form.cleaned_data['password'],
                                            email=registration_form.cleaned_data['email'])
            # Don't save the my_user_form instance
            my_user_inst = my_user_form.save(commit=False)
            # Assign the saved User(User object) before to the user attribute of the my_user_inst form
            my_user_inst.user = user
            # Once the user attribute has been assigned then save the form.
            my_user_inst.save()

            # Some debugging
            # print(my_user_form.cleaned_data)
            # print(registration_form.cleaned_data)

            # later functionality to be added
            # Send verification email
            # redirect to login page
            return redirect('/accounts/register_success')
        else:
            return render(request, 'accounts/user_registration.html',
                          {'registration_form': registration_form, 'my_user_form': my_user_form})
    # if a GET (or any other method) we'll create a blank form
    else:
        registration_form = UserRegistrationForm()
        my_user_form = MyUsersForm()
        my_user_form.fields['created_by'] = forms.ModelChoiceField(User.objects.filter(username=request.user))
        return render(request, 'accounts/user_registration.html',
                      {'registration_form': registration_form, 'my_user_form': my_user_form})


def user_registration_success(request):
    return render(request, 'accounts/user_registration_success.html')


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

