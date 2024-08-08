from django import forms

class utmForm(forms.Form):
    UTM_ZONES = [
        ('46N', 'Zone 46N'),
        ('47N', 'Zone 47N'),
        ('48N', 'Zone 48N'),
        ('49N', 'Zone 49N'),
        ('50N', 'Zone 50N'),
        ('51N', 'Zone 51N'),
    ]

    x = forms.FloatField(label='X Coordinate', required=True)
    y = forms.FloatField(label='Y Coordinate', required=True)
    utm = forms.ChoiceField(label='UTM Zone', choices=UTM_ZONES, required=True)

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
