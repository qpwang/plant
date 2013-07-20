from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    data = {}
    return render_to_response('index.html', data,
            context_instance=RequestContext(request))
