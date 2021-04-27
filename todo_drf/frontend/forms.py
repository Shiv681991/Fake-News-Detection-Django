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

STATES = (('in-py', "Puducherry"),
         ('in-ld', "Lakshadweep"),
         ('in-wb', "West_Bengal"),
         ('in-or', "Orissa"),
         ('in-br', "Bihar"),
         ('in-sk', "Sikkim"),
         ('in-ct', "Chattisgarh"),
         ('in-tn', "TN"),
         ('in-mp', "MP"),
         ('in-2984', "Gujrat"),
         ('in-ga', "Goa"),
         ('in-nl', "Nagaland"),
         ('in-mn', "Manipur"),
         ('in-ar', "Arunachal_Pradesh"),
         ('in-mz', "Mizoram"),
         ('in-tr', "Tripura"),
         ('in-3464', "Daman_and_Diu"),
         ('in-dl', "Delhi"),
         ('in-hr', "Haryana"),
         ('in-ch', "Chandigarh"),
         ('in-hp', "HP"),
         ('in-jk', "J&K"),
         ('in-kl', "Kerela"),
         ('in-ka', "Karnataka"),
         ('in-dn', "Dadra_and_Nagar_Haveli"),
         ('in-mh', "Maharashtra"),
         ('in-as', "Assam"),
         ('in-ap', "AP"),
         ('in-ml', "Meghalaya"),
         ('in-pb', "Punjab"),
         ('in-rj', "Rajasthan"),
         ('in-up', "UP"),
         ('in-ut', "Uttaranchal"),
         ('in-jh', "Jharkhand"))



class locationForm(forms.Form):
    location = forms.ChoiceField(choices=LOCATIONS, required=True)

class stateForm(forms.Form):
    stateName = forms.ChoiceField(choices=STATES, required=True)

class UploadFileForm(forms.Form):
    file = forms.FileField(required=False)

check_choices = (("1", "ENT"),
                 ("2", "CLS"))

class in_textForm(forms.Form):
    in_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 70}))
    check_fields = forms.ChoiceField(choices = check_choices, widget=forms.RadioSelect)
