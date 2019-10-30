from django import forms
from . models import Line, Station


class LineForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Hello world'}))
    line_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    night_route = forms.BooleanField(
        widget=forms.TextInput(attrs={'type': 'checkbox', 'class': 'form-check-input'}))

    class Meta:
        model = Line
        fields = ['name', 'line_number', 'night_route']


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['lat', 'lng', 'station_name', ]


class ContactForm(forms.Form):
    station_name = forms.CharField(max_length=30, min_length=3)
    lat = forms.DecimalField(decimal_places=4, max_digits=10)
    lng = forms.DecimalField(decimal_places=4, max_digits=10)
