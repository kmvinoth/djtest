from django.forms import ModelForm
from .models import User, UserProfile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob', 'nickname')

