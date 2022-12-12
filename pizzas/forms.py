from django import forms

from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping_name']
        labels = {'topping_name':''}

        widgets = {'topping_name':forms.Textarea(attrs={'cols':80})}