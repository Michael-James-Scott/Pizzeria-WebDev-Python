from django import forms 
from .models import Pizza, Comment, Topping

class addPizza(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        labels = {'text': 'Pizza:'}

class addComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comment:'}

        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class addTopping(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['top_choice']
        labels = {'top_choice': 'Topping:'}

        