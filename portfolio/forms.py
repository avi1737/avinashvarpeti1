from django import forms


class getInTouchForm(forms.Form):
    fullname = forms.CharField(label='Full Name',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Your Email',max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(label='Your Mobile no.',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    msg = forms.CharField(label='Your Messsage',widget=forms.TextInput(attrs={'class':'form-control'}))
