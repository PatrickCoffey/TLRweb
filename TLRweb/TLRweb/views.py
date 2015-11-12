from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.contrib.messages import constants as messages

# Create your views here.

def home(request):
    template = loader.get_template('templates/example.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))