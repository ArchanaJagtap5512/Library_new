
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookForm(UserCreationForm):
    email = forms.EmailField(required=True)
    frist_name = forms.CharField(max_length = 100 , required=True)
    last_name = forms.CharField(max_length = 100 , required=True)


    class meta:
        model = User
        fields = ("firs_name", "last_name","username","email","password","password2")

    def save(self , commit = True): # over-ridden save method from UserCreation
        user =  super(BookForm , self).save(commit = False)
        # print(user. _dict_)
        user.email = self.cleaned_data['email']
        user.frist_name = self.cleaned_data['frist_name']
        user.last_name = self


