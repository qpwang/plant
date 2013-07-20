from django.shortcuts import render_to_response
from django.template import RequestContext
from plant.models import Plant

def home(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    data = {'plant': plant}
    return render_to_response('index.html', data,
            context_instance=RequestContext(request))
