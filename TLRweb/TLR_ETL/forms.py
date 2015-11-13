from django import forms



class etl_form(forms.Form):
    csv_file = forms.CharField(label='location of CSV file to load', 
                               max_length=100)