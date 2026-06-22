from django import forms
from website.models import Contact



class NameForm(forms.Form):
    name = forms.CharField(max_length=254)
    email = forms.EmailField()
    subject = forms.CharField(max_length=254)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = ['name','email']
        fields = '__all__'  
        # tamam field ha be ghir az name  
        # exclude = ['name']
    