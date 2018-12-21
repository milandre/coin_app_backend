"""User Forms.

This file has the forms used
for user operations like
login and sign up.
"""

from django import forms
from django.contrib.auth import forms as auth_forms
from django.core.validators import RegexValidator
from account.models import Account
from currency.models import Currency
from .models import Client



class SignUpAdminForm(auth_forms.UserCreationForm):
    """SignUpForm

    A form for admin user sign up. Inherit from
    UserCreationForm
    """

    password1 = forms.CharField(
        label='Password', min_length=6, max_length=16,
        validators=[
            RegexValidator(
                regex='^([\w.*+-]){6,16}$',
                message='Enter a valid password. This value may contain only letters, numbers and */./+/-/_ '
                          'characters, and at least 6 characters and at most 16 characters.',
                code='invalid_new_password1'
            )
        ],
        widget=forms.PasswordInput(
            attrs={
                'title':'Enter a valid password. This value may contain only letters, numbers and */./+/-/_ '
                           'characters, and at least 6 characters and at most 16 characters.',
                'required pattern': '^([\w.*+-]){6,16}$'
            }
        )
    )

    password2 = forms.CharField(
        label='Password confirmation', min_length=6, max_length=16,
        validators=[
            RegexValidator(
                regex='^([\w.*+-]){6,16}$',
                message='Please enter the same password as above.',
                code='invalid_new_password2'
            )
        ],
        widget=forms.PasswordInput(
            attrs={
                'title': 'Please enter the same password as above.',
                'required pattern': '^([\w.*+-]){6,16}$'
            }
        )
    )

    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Email',
                                                            'required': 'required'
                            }))

    class Meta(auth_forms.UserCreationForm):
        model = Client
        fields = '__all__'


    def clean_email(self):
        email = self.cleaned_data['email']
        email_exists = Client.objects.filter(email=email)
        if email_exists:
            self.add_error('email', 'This email is already registered.')
        return email

    def __init__(self, *args, **kwargs):
        super(SignUpAdminForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True


class SignUpForm(SignUpAdminForm):
    """SignUpForm

    A form for user sign up. Inherit from
    SignUpAdminForm
    """
    currency = forms.ModelChoiceField(queryset=Currency.objects.all())

    class Meta:
        model = Client
        fields = ('email', 'first_name', 'last_name')


class ClientUpdateForm(forms.ModelForm):
    """
        A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = auth_forms.ReadOnlyPasswordHashField()

    class Meta:
        model = Client
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]