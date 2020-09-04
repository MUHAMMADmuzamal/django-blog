from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.
def blogHome(request):
   allposts = Post.objects.all()
   context = allposts
   context = {'allposts':context}
   return render(request,'blog/blogHome.html',context)
   # return HttpResponse("Blog HOm-e file")

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/blogPost.html',context)
    #return HttpResponse("Blog POst file "+slug)

