from django import forms


class AddProduct(forms.Form):
    add_quantity = forms.IntegerField()


class DateInput(forms.DateInput):
    input_type = 'date'


class GeeksForm(forms.Form):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
