from django import forms
from .models import *


class HomePageForm(forms.ModelForm):
    img1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img3 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img4 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = HomePage
        fields = ['img1', 'img2', 'img3', 'img4']


class ServicePageForm(forms.ModelForm):
    img1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img3 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = ServicePage
        fields = ['img1', 'img2', 'img3', 'video']


class BlogPageForm(forms.ModelForm):
    img1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img3 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = ServicePage
        fields = ['img1', 'img2', 'img3', 'video']


class ServicesPageForm(forms.ModelForm):
    img1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = ServicePage
        fields = ['img1', 'img2']


class ContactPageForm(forms.ModelForm):
    img1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))
    img2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = ServicePage
        fields = ['img1', 'img2']
