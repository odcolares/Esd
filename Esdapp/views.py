from django.shortcuts import render, redirect
from Esdapp.forms import EsdForm
from Esdapp.models import Esd

# Create your views here.
def home(request):
    data = {}
    data['db'] = Esd.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = EsdForm()
    return render(request, 'form.html', data)

def create(request):
    form = EsdForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = Esd.objects.get(pk=pk)
    data['form'] = EsdForm(instance=data['db'])
    return render(request, 'form.html', data)

def delete(request, pk):
    db = Esd.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def update(request, pk):
    data = {}
    data['db'] = Esd.objects.get(pk=pk)
    form = EsdForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save() 
        return redirect ('home')

def view(request, pk):
    data = {}
    data['db'] = Esd.objects.filter(pk=pk)
    return render(request, 'view.html', data)
