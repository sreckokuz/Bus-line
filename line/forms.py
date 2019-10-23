from django import forms
from . models import Line


class LineForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Hello world'}))
    # line_number = forms.IntegerField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.DecimalField()

    class Meta:
        model = Line
        fields = [
            'name',
            'line_number'
        ]
