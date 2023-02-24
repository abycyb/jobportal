from django import forms
from django.forms import ModelForm,DateField,CharField,EmailField,IntegerField
from .models import *


class postjobform(forms.Form):

    cname=forms.CharField(max_length=30)
    email=forms.EmailField()
    jtitle=forms.CharField(max_length=50)
    wtype=forms.CharField(max_length=30)
    expreq=forms.CharField(max_length=30)
    jtype=forms.CharField(max_length=30)


class formempreg(forms.Form):
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    dob=forms.DateField()
    quali=forms.CharField(max_length=50)
    phno=forms.IntegerField()
    password=forms.CharField(max_length=50)
    cpassword=forms.CharField(max_length=50)


class emplogform(forms.Form):
    m=forms.EmailField()
    p=forms.CharField(max_length=50)


class formemp(forms.ModelForm):
    class Meta:
        model= modelempreg1
        fields="__all__"


class applyform(forms.Form):
    compnm = forms.CharField(max_length=50)
    jobtitle = forms.CharField(max_length=50)
    empname = forms.CharField(max_length=50)
    empemail = forms.EmailField()
    empph = forms.IntegerField()
    exp = forms.CharField(max_length=100)
    pdf = forms.FileField()
