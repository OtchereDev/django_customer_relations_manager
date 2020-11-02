from django.forms import ModelForm
from .models import Permission,User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.db import transaction

from django.contrib.auth import get_user_model
User = get_user_model()

class OrderForm(ModelForm):
    class Meta:
        model = Permission
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']


# ----------------changes



# from classroom.models import Student, Subject, User

class UserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields=['username','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_user = True
        user.save()
        return user




# -----------teachers


class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user