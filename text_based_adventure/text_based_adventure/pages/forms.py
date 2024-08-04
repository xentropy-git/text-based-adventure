from django import forms

class ActionForm(forms.Form):
    action = forms.CharField(
        label='Your Action',
        widget=forms.TextInput(attrs={'placeholder': 'Type your action here...', 'class': 'form-control'})
    )
