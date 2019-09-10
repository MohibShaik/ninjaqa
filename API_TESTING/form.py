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
    Url = forms.URLField(label='url', max_length=100)
    Api = forms.CharField()

    def clean(self):
       cleaned_data = super(APIForm, self).clean()
       Url = cleaned_data.get('Url')
       Api = cleaned_data.get('Api')


   

