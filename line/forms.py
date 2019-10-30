from django import forms
from . models import Line, Station


class LineForm(forms.ModelForm):
    # styling input fields
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    line_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    distance = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Distance in [km]'}))

    class Meta:
        model = Line
        fields = ['name', 'line_number', 'distance']


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['lat', 'lng', 'station_name', ]


class AdditionalForm(forms.Form):
    station_name = forms.CharField(max_length=30, min_length=3)
    lat = forms.DecimalField(decimal_places=4, max_digits=10)
    lng = forms.DecimalField(decimal_places=4, max_digits=10)
