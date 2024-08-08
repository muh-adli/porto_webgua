from django import forms

class utmForm(forms.Form):
    UTM_ZONES = [
        ('EPSG:32646', 'Zone 46N'),
        ('EPSG:32647', 'Zone 47N'),
        ('EPSG:32648', 'Zone 48N'),
        ('EPSG:32649', 'Zone 49N'),
        ('EPSG:32650', 'Zone 50N'),
        ('EPSG:32651', 'Zone 51N'),
    ]

    x = forms.FloatField(label='X Coordinate', required=True)
    y = forms.FloatField(label='Y Coordinate', required=True)
    zone = forms.ChoiceField(label='UTM Zone', choices=UTM_ZONES, required=True)

class wgsForm(forms.Form):
    lattitude = forms.FloatField(
        label='Lattitude',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control my-1',
            'step': 'any'  # Allows for floating-point numbers
        })
    )
    longitude = forms.FloatField(
        label='Longitude',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control my-1',
            'step': 'any'  # Allows for floating-point numbers
        })
    )
