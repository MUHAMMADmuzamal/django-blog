from django.shortcuts import render,HttpResponse,redirect
from  home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout
# Create your views here.
def home(request):
    #return HttpResponse(" index file")
    return render(request,'home/index.html')


def about(request):
    messages.success(request, 'This is about.')
    return render(request,'home/about.html')
 #   return HttpResponse(" home/about file")

 
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) <3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please fill the forms correctly.')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent.')
    return render(request,'home/contact.html')
 #   return HttpResponse(" home/contact file")
def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allposts=Post.objects.none()
    else:
         allpostsTitle = Post.objects.filter(titile__icontains=query)
         allpostsContent = Post.objects.filter(content__icontains=query)
         allposts =  allpostsTitle.union(allpostsContent)
    if allposts.count() == 0:
        messages.warning(request, 'No search results found. Please refine your query.')
    params = {'allPosts':allposts,'query':query}
    return render(request,'home/search.html',params)
 #   return HttpResponse(" home/about file")


def handleSignup(request):
     if request.method == 'POST':
         username = request.POST['username']
         firstname = request.POST['firstname']
         lastname = request.POST['lastname']
         email = request.POST['email']
         pass1 = request.POST['pass1']
         pass2 = request.POST['pass2']

         #check for errorneous inputs
         if len(username) > 10:
            messages.error(request, 'Username must be under 10 Characters.')
            return redirect('Home')
         if pass1 != pass2:
            messages.error(request, 'Password do not match.')
            return redirect('Home')
         if not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers.')
            return redirect('Home')
         #create the user
         myuser = User.objects.create_user(username,email,pass1)
         myuser.first_name = firstname
         myuser.last_name = lastname
         myuser.save()
         messages.success(request,"Your iCoder account has been successfully created")
         return redirect('/')
     else:  
        return HttpResponse('404 - Not Found')
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('Home')
        else:
            messages.error(request,"Invalid Credentials Please try again")
            return redirect('Home')
def handleLogout(request):
   # if request.method == 'POST':
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('Home')
    