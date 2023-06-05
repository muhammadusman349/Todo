
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email") 
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")


























# from django import forms  
# from django.contrib.auth.models import User,AbstractBaseUser
# from django.contrib.auth.forms import UserCreationForm  
# from django.core.exceptions import ValidationError  

# class CustomUserCreationForm(AbstractBaseUser):  
#     username = forms.CharField(label='username', min_length=5, max_length=150)  
#     first_name = forms.CharField(label='first_name')  
#     last_name = forms.CharField(label='last_name')  
#     # phone_num = forms.IntegerField()  
#     # address = forms.CharField(label='address')  
#     email = forms.EmailField(label='email')  
#     is_owner = forms.BooleanField(label='is_owner') 
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
#     def username_clean(self):  
#         username = self.cleaned_data['username'].lower()  
#         new = User.objects.filter(username = username)  
#         if new.count():  
#             raise ValidationError("User Already Exist")  
#         return username  
  
#     def email_clean(self):  
#         email = self.cleaned_data['email'].lower()  
#         new = User.objects.filter(email=email)  
#         if new.count():  
#             raise ValidationError(" Email Already Exist")  
#         return email  
  
#     def clean_password2(self):  
#         password1 = self.cleaned_data['password1']  
#         password2 = self.cleaned_data['password2']  
  
#         if password1 and password2 and password1 != password2:  
#             raise ValidationError("Password don't match")  
#         return password2  
  
#     def save(self, commit = True):  
#         user = User.objects.create_user(
#             username= self.cleaned_data['username'],  
#             email=self.cleaned_data['email'],  
#             first_name=self.cleaned_data['first_name'], 
#             last_name=self.cleaned_data['last_name'],
#             # is_owner=self.cleaned_data['is_owner'],
            
#             # phone_num=self.cleaned_data['phone_num'],
#             # address=self.cleaned_data['address'],
#             password=self.cleaned_data['password1'],
#         )  
#         return user  