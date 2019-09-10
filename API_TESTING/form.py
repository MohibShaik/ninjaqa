# from django import forms
# from .models import Requtest

from django import forms


Method_choices=[
    ['GET','GET'],
    ['POST','POST'],
    ['PUT','PUT'],
    ['DELETE','DELETE'],
]




# API Form
class APIForm(forms.Form):
    Method = forms.ChoiceField(choices = Method_choices)
    URL = forms.URLField(label='URL', max_length=100)
    PATH = forms.CharField(max_length=250)


    def clean(self):
       cleaned_data = super(APIForm, self).clean()
       URL = cleaned_data.get('URL')
       PATH= cleaned_data.get('PATH')


   

