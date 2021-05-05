from django.shortcuts import render, redirect
from Esdapp.forms import esdForm
from Esdapp.models import esd

# Create your views here.
def home(request):
    data = {}
    data['db'] = esd.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = esdForm()
    return render(request, 'form.html', data)

def create(request):
    form = esdForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')