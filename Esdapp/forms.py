from django.forms import ModelForm
from Esdapp.models import esd

# Create the form class.
class esdForm(ModelForm):
     class Meta:
         model = esd
         fields = ['nome', 'setor', 'matricula']