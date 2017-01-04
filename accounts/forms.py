from django.forms import ModelForm
from .models import User, UserProfile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dob', 'nickname']


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_username(self):
        pass

    def clean_email(self):
        pass

