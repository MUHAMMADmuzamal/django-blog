from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(" index file")

def contact(request):
    return HttpResponse(" contact file")

def about(request):
    return HttpResponse(" about file")
