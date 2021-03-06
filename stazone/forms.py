from django import forms
from .models import Image,Comment,Profile

class StazoneLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption']

class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = ['text']
