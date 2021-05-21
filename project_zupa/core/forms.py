from django import forms

class KontaktForm(forms.Form):
    name =  forms.CharField(label='Vaše ime:' ,max_length=100)
    email  = forms.EmailField(label='Vaš e-mail:')
    subject = forms.CharField(label='Naslov:' ,max_length=100)
    message = forms.CharField(label='Vaša poruka:' ,widget=forms.Textarea)
