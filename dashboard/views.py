from django.shortcuts import render
from .models import DjangoHub
from .forms import ResourcesForm

def data_read(request):
    context = {'data_read':DjangoHub.objects.all()}
    return render(request, "data_read.html", context)

def data_form(request, id = None):
    if request.method == POST:
        if id == None:
            form = ResourcesForm(request.POST)
        else:
            resources = DjangoHub.objects.get(pk = id)
            form = ResourcesForm(request.POST, instance = resources)
        if form.is_valid():
            form.save()
        return redirect('/data')

    else:
        if id == None:
            form = ResourcesForm()
        else:
            resources = DjangoHub.objects.get(pk = id)
            form = ResourcesForm(instance = resources )
        return render(request, "data_form.html", {'form':form})

def data_delete(request, candidate_id):
    resources = DjangoHub.objects.get(id = resources_id)
    resources.delete()
    return redirect('/data')