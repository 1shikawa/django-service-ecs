from django.shortcuts import render
from .models import Sample
from django.http import HttpResponse

# Create your views here.
# def hello(request):
#   return HttpResponse('Hello, Django Django !!')

from django.views.generic import ListView
class SampleListView(ListView):
    model = Sample
    context_object_name = "sample"
    template_name = 'sample_list.html'
