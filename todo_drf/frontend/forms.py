from django import forms

LOCATIONS = (
    ('OTR', 'Other'),
    ('AMR', 'Amritsar'),
    ('SNR', 'Sri Nagar'),
    ('CHN', 'Chandigadh'),
    ('DLI', 'Delhi'),
    ('LKO', 'Lucknow'),
    ('VNS', 'Varanasi'),
    ('JPR', 'Jaipur'),
    ('AMD', 'Ahmedabad'),
    ('KPR', 'Kanpur'),
    ('IDR', 'Indore'),
    ('KTA', 'Kolkata'),
    ('RCH', 'Ranchi'),
    ('PNE', 'Pune'),
    ('MBI', 'Mumbai'),
    ('GWT', 'Guwahati'),
    ('HBD', 'Hyderabad'),
    ('BLR', 'Bangalore')
)



class locationForm(forms.Form):
    location = forms.ChoiceField(choices=LOCATIONS, required=True)

class UploadFileForm(forms.Form):
    file = forms.FileField(required=False)

check_choices = (("1", "ENT"),
                 ("2", "CLS"))

class in_textForm(forms.Form):
    in_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 70}))
    check_fields = forms.ChoiceField(choices = check_choices, widget=forms.RadioSelect)
