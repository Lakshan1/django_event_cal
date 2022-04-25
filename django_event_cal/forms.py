from django import forms
from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
    class Meta:
        model =Events
        fields = '__all__'
        exclude = ['created_at'] 

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['slug'].required = False

    event_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter event name..'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'hidden','class':'form-control','placeholder':'Enter year in number..'}))
    month = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden','class':'form-control','placeholder':'Enter month in name..'}))
    date = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'hidden','class':'form-control','placeholder':'Enter date..'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'description..'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))

class AdEventForm(ModelForm):
    class Meta:
        model =Events
        fields = '__all__'
        exclude = ['created_at','slug'] 

    event_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter event name..'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'hidden','class':'form-control','placeholder':'Enter year in number..'}))
    month = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden','class':'form-control','placeholder':'Enter month in name..'}))
    date = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'hidden','class':'form-control','placeholder':'Enter date..'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'description..'}))