from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras


# Create your views here.
def blogHome(request):
   allposts = Post.objects.all()
   context = allposts
   context = {'allposts':context}
   return render(request,'blog/blogHome.html',context)
   # return HttpResponse("Blog HOm-e file")

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
       if reply.parent.sno not in repDict.keys():
          repDict[reply.parent.sno] =  [reply]
       else:
         repDict[reply.parent.sno].append(reply)
   #  print(comments,replies)
   #  print(repDict)
    context = {'post':post,'comments':comments,'user':request.user,'replyDict':repDict}
    return render(request,'blog/blogPost.html',context)
    #return HttpResponse("Blog POst file "+slug)


def postComment(request):
   if request.method == 'POST':
      
      comment =  request.POST.get("comment")
      user =  request.user
      postsno =  request.POST.get("postsno")
      
      post = Post.objects.get(sno=postsno)
      parentsno =  request.POST.get('parentSno')
      
      if parentsno == "":
         comment = BlogComment(comment=comment,user=user,post=post)
         messages.success(request,"Your comment has been posted sucessfully")
      else:
         parent = BlogComment.objects.get(sno=parentsno)
         comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
         messages.success(request,"Your reply has been posted sucessfully")
      comment.save()
   return redirect(f"/blog/{post.slug}")

