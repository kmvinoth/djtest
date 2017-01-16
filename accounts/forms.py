from django import forms
from .models import User, UserProfile, MyUsers


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dob', 'nickname']


class MyUsersForm(forms.ModelForm):

    class Meta:
        model = MyUsers
        fields = ['created_by', ]

    def clean_created_by(self):
        try:
            created_by = self.cleaned_data.get('created_by')
            return created_by
        except User.DoesNotExist:
            raise forms.ValidationError('The project admin does not exist')


class UserRegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Figure out how super works...!
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Making email field required for user registration form
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_username(self):
        """
        Check the new username versus the existing username in the database and throws a validation error
        if it matches, if not return's the cleaned username (new_username)
        """

        new_username = self.cleaned_data.get('username')
        try:
            existing_username = User.objects.get(username__iexact=new_username)  # Remember it is a User object
        except User.DoesNotExist:
            return new_username
        raise forms.ValidationError('The username %(value)s already exists. Please try another one',
                                    params={'value': existing_username.username}, code='username exists')

    def clean_email(self):
        """
        Check the new email versus the existing email in the database and throws a validation error
        if it matches, if not return's the cleaned email (new_email)
        """

        new_email = self.cleaned_data.get('email')
        try:
            existing_user = User.objects.get(email__exact=new_email)  # exact query for the email address
            existing_email = existing_user.email
        except User.DoesNotExist:
            return new_email
        raise forms.ValidationError('The email %(value)s address is already registered with us',
                                    params={'value': existing_email}, code='email exists')
