from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse

# Create your views here.

def home(request):
    template = loader.get_template('templates/bs_dash_base.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))