from django import forms


class User_Signup(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'username','placeholder':'Username'}),required=True)
    firstname = forms.CharField(widget=forms.TextInput(attrs={'name':'firstname','placeholder':'Firstname'}),required=True)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'name':'lastname','placeholder':'Lastname'}),required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'name':'email','placeholder':'Email'}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name':'password','placeholder':'Password'}),required=True)

   
class Create_med_form(forms.Form):
    med_name = forms.CharField(widget=forms.TextInput(attrs={"name":"med_name","placeholder":"Medicine Name"}),required=True)
    med_price = forms.IntegerField(widget=forms.NumberInput(attrs={"name":"med_price","placeholder":"Price"}),required=True)
    disease = forms.CharField(widget=forms.TextInput(attrs={"name":"disease","placeholder":"Disease"}),required=True)


class Edit_med_form(forms.Form):
    med_name = forms.CharField(widget=forms.TextInput(attrs={"name":"med_name","placeholder":"Medicine Name"}),required=True)
    med_price = forms.IntegerField(widget=forms.NumberInput(attrs={"name":"med_price","placeholder":"Price"}),required=True)
    disease = forms.CharField(widget=forms.TextInput(attrs={"name":"disease","placeholder":"Disease"}),required=True)
