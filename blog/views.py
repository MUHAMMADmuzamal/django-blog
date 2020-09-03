from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("Blog HOm-e file")

def blogPost(request,slug):
    return HttpResponse("Blog POst file "+slug)

