from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('chef', 'Chef')
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Select Your Role")
    full_name = forms.CharField(
        max_length=100,
        required=False,
        label="Full Name"
    )
    admission_number = forms.CharField(
        max_length=20,
        required=False,
        label="Admission No. (ID)"
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role', 'full_name', 'admission_number']

    def save(self, commit=True):
        user = super().save(commit=commit)
        role = self.cleaned_data['role']
        full_name = self.cleaned_data.get('full_name', '')
        admission_number = self.cleaned_data.get('admission_number', '')
        UserProfile.objects.create(
            user=user,
            role=role,
            full_name=full_name,
            admission_number=admission_number
        )
        return user
