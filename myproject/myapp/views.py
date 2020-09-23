#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse          #Main index file Http Responds
from django.views.generic import TemplateView   #classes Template Views views 

#classes Template view 
class AboutView(TemplateView):
    template_name = "about.html"

#main index file
def index(request):
    return HttpResponse("<h1> Hello World </h1>")