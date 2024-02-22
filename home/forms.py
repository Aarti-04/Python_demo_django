from django import forms
class Nameform(forms.Form):
    your_name=forms.CharField(label="your name",max_length=100 )
    