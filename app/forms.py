from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'CompanyName')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'CompanyName')


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2", "CompanyName", "Address", "BillingDetails", "Plan", "PhoneNumber",
                  ]

        widget = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class productform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model=Product
        fields=['name']


class lang_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = lang
        fields = ['name']



class langpro_form(forms.ModelForm):

    title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subtitle=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    video=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    txt=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # product=forms.CharField(widget = forms.HiddenInput(), required = False)
    def __init__(self, *args, **kwargs):
        super(langpro_form, self).__init__(*args, **kwargs)
        self.fields['language'].widget.attrs['class'] = 'form-control'
    #     # self.fields['product'].widget.attrs['value'] = Product.objects.get(pk=self.pr).id

    class Meta:
        model = language
        fields = ['language','title','subtitle','txt','image','video']



