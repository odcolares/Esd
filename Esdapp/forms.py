from django.forms import ModelForm
from Esdapp.models import Esd

# Create the form class.
class EsdForm(ModelForm):
     class Meta:
         model = Esd
         fields = ['nome', 'matricula', 'setor']