from django import forms
class Imageuploadform(forms.Form):
    image=forms.ImageField()