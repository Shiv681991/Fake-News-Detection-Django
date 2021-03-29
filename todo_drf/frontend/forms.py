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