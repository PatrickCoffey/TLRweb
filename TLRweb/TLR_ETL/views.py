from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import etl_form

import time

# Create your views here.

def etl(request):
    template = loader.get_template('templates/etl.html')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = etl_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            messages.info(request, "Please wait while your data is processed!")
            messages.info(request, "Reading data from " + request.POST.get('csv_file'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = etl_form()    
    context = RequestContext(request, {'form': form})
    return HttpResponse(template.render(context))