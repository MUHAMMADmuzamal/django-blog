from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse(" index file")
    return render(request,'home/index.html')

def contact(request):
    return render(request,'home/contact.html')
 #   return HttpResponse(" home/contact file")

def about(request):
    return render(request,'home/about.html')
 #   return HttpResponse(" home/about file")
