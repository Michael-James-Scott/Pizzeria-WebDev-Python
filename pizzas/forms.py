from django import forms 
from .models import Pizza, Comment

class addPizza(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        labels = {'text': ''}

class addComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comment:'}

        widgets = {'text': forms.Textarea(attrs={'cols':80})}