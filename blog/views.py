from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
   return render(request,'blog/blogHome.html')
   # return HttpResponse("Blog HOm-e file")

def blogPost(request,slug):
    return render(request,'blog/blogPost.html')
    #return HttpResponse("Blog POst file "+slug)

