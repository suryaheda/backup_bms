from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(label='', max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Type your question...'}))