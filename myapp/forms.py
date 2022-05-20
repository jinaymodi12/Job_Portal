from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *


class  LoginForm(AuthenticationForm):
    username=forms.CharField(label='Username',error_messages={'password':{'required':'Password Required'}})
    password=forms.CharField(label='Password',widget=forms.PasswordInput(),error_messages={'password':{'required':'Password Required'}})

class EditForm(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','email','gender','companyname']
        Widget={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.ChoiceField(),
            'companyname': forms.TextInput(attrs={'class':'form-control'}),

        }

class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','email','gender','companyname']
        Widget={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailField(),
            'gender': forms.ChoiceField(),
            'companyname': forms.TextInput(attrs={'class':'form-control'}),
            

        }
    
#<<<<<<<<<<<<< HR-JOB POST FORM >>>>>>>>>>>>>>>>>>>>#

class JobForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['address','salary','position','vacancy','category','experience','description']
        label={'address':'ADDRESS','salary':'SALARY','category':'CATEGORY','experience':'EXPERIENCE','description':'DESCRIPTION'}
        Widget={
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.Select(attrs={'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'experience':forms.Select(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
        }
class JobEditForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['address','salary','position','vacancy','category','experience','description']



#<<<<<<<<<<<<<<<<<<<<<<<<<<< Candidate Profile >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

class candidateform(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['name','email','dob','gender','mobile','resume']
        label={'name':'NAME','dob':'DATE OF BIRTH','gender':'GENDER','mobile':'MOBILE','email':'EMAIL'}
        Widget={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailField(),
            'dob' : forms.DateField(),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'resume' : forms.FileField()
           
            
        }