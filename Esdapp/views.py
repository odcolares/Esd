from django.shortcuts import render
from Esdapp.forms import esdForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = esdForm()
    return render(request, 'form.html', data)