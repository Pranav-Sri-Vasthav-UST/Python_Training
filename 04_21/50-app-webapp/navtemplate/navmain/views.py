from django.shortcuts import render, redirect
from .forms import IncidentForm
from .models import Incident
from django.db.models import Count

# Create your views here.

def dashboard(request):
    data = Incident.objects.values('incident_type').annotate(count=Count('id')) # => SQL GROUPBY OPERATION WITH COUNT
    labels = [ d['incident_type'].capitalize() for d in data]
    counts = [d['count'] for d in data]
    context = {
        'labels': labels,
        'counts': counts
    }
    return render(request, 'navmain/dashboard.html', context=context)


def incidents(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incidents')
    else:
        form = IncidentForm()
    context = {
        'form': form
    }
    return render(request, 'navmain/incidents.html', context=context)

 
def customers(request):
    incidents = Incident.objects.all().order_by('timestamp')
    context = {
        "incidents": incidents
    }
    return render(request, 'navmain/customers.html', context=context)

 
def about(request):
    return render(request, 'navmain/about.html')   