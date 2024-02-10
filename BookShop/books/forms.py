from django import forms

class Addproducrtorecipe(forms.Form):

    recipe= forms.CharField(label="write recipe ", max_length= 10)
    product = forms.CharField(label="write product ", max_length= 10)
    weight = forms.CharField(label="write weight", max_length= 10)