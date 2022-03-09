from django import forms

class Feedbackform(forms.Form):
    name=forms.CharField(max_length=35)
    age = forms.IntegerField()
    add1 = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

