from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Resources
from .forms import ResourcesForm

# Create your views here.
def index(request):
  return render(request, 'resources/index.html', {
    'resources': Resources.objects.all()
  })

def view_resources(request, id):
  resources = Resources.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = ResourcesForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      link= form.cleaned_data['link']
      tags = form.cleaned_data['tags']
      format = form.cleaned_data['format']
      difficulty = form.cleaned_data['difficulty']
      time = form.cleaned_data['time']            

      new_resources = Resources(
      name = name,
      link = link,
      tags = tags,
      format = format,
      difficulty = difficulty,
      time = time  
      )
      new_resources.save()
      return render(request, 'resources/add.html', {
        'form': ResourcesForm(),
        'success': True
      })
  else:
    form = ResourcesForm()
  return render(request, 'resources/add.html', {
    'form': ResourcesForm()
  })

def edit(request, id):
  if request.method == 'POST':
    resources = Resources.objects.get(pk=id)
    form = ResourcesForm(request.POST, instance=resources)
    if form.is_valid():
      form.save()
      return render(request, 'resources/edit.html', {
        'form': form,
        'success': True
      })
  else:
    resources = Resources.objects.get(pk=id)
    form = ResourcesForm(instance=resources)
  return render(request, 'resources/edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    resources = Resources.objects.get(pk=id)
    resources.delete()
  return HttpResponseRedirect(reverse('index'))