from django.shortcuts import render
from django.views.generic import TemplateView
from carapp.forms import *

# Create your views here.
class Homeview(TemplateView):
    template_name="index2.html"
    
def contact(request):
   return render(request, 'index.html')

def bloges(request):
   return render(request, 'index3.html')

def product(request):
   return render(request, 'index4.html')

def home(request):
   return render(request, 'index2.html')

def apponment1(request):
   return render(request, 'index5.html')


def insertcontact(request):
   if request.method=='POST':
      form=contactform(request.POST)
      if form.is_valid():
         form.save()
         return render(request,"index.html")

def insertapponment(request):
   if request.method=='POST':
      form=apponmentform(request.POST)
      if form.is_valid():
         form.save()
      return render(request,"index5.html")



