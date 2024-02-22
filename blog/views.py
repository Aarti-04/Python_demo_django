# '''Django REST framework'''

# from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse
# from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework.decorators import api_view,permission_classes

# # from django.contrib.auth.decorators import login_required
# from blog.models import Blog
# from django.contrib import messages

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def home(request):
#     posts = Blog.objects.all()
#     return render(request,"home.html",{"posts":posts})
# @IsAuthenticated()
# def create_post(request):
#     if request.method=="POST":
#         title=request.POST.get("title")
#         content=request.POST.get("content")
#         # userid=request.POST.get("userid")
#         userid= request.user
#         # print(userid)
#         try:
#             blog = Blog(title=title,content=content,userid=userid)
#             # print(blog)
#             blog.save()
#         except:
#             # print(blog)
#             messages.warning(request, "Something went wrong post not created")
#         else:
#             messages.success(request,"Post Created successfully")
#             return redirect("/blog/")

#     return render(request,"post.html")

# def delete_post(request,id):
#     # blog = Blog.objects.get(pk=id)
#     # blog.delete()
#     try:
#         blog=get_object_or_404(Blog,pk=id)
#         blog.delete()
#     except:
#         messages.warning(request, "Something went wrong post not deleted")
#     else:
#         messages.success(request, "Post deleted")
#     return redirect("/blog/")

# def edit_post(request,id):
    
#     if request.method=="POST":
#         id=request.POST.get("id")
#         print(id)
#         blog= Blog.objects.get(id=id)
#         title=request.POST.get("title")
#         content=request.POST.get("content")
#         try:
#             blog.title=title
#             blog.content=content
#             blog.save()
#         except Exception as e:
#             messages.warning(request, f"Something went wrong post not created {str(e)}")
#         else:
#             messages.success(request,"Post Updated successfully")
#             return redirect("/blog/")
#     blog=Blog.objects.get(pk=id) 
#     return render(request,"post.html",{"post":blog})

'''without REST Framework'''
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import Blog
'''Django signals.......'''
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .forms import UploadFile
from blog.models import Mymodel


# from django.contrib.auth.decorators import login_required
from blog.models import Blog
from django.contrib import messages

@receiver(pre_save,sender=Blog)
def call_blog_beforecreate(sender,instance,**kwargs):
    print("Blog is going to create")

def home(request):
    
    posts = Blog.objects.all()
    return render(request,"home.html",{"posts":posts})

def create_post(request):

    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        # userid=request.POST.get("userid")
        userid= request.user
        print(type(userid))
        try:
            blog = Blog(title=title,content=content,userid=userid)
            # print(blog)
            blog.save()
        except:
            # print(blog)
            messages.warning(request, "Something went wrong post not created")
        else:
            messages.success(request,"Post Created successfully")
            return redirect("/blog/")

    return render(request,"post.html")
@login_required(login_url="/login/")
def delete_post(request,id):
    # blog = Blog.objects.get(pk=id)
    # blog.delete()
    try:
        blog=get_object_or_404(Blog,pk=id)
        blog.delete()
    except:
        messages.warning(request, "Something went wrong post not deleted")
    else:
        messages.success(request, "Post deleted")
    return redirect("/blog/")
@login_required(login_url="/login/")
def edit_post(request,id):
    
    if request.method=="POST":
        id=request.POST.get("id")
        print(id)
        blog= Blog.objects.get(id=id)
        title=request.POST.get("title")
        content=request.POST.get("content")
        try:
            blog.title=title
            blog.content=content
            blog.save()
        except Exception as e:
            messages.warning(request, f"Something went wrong post not created {str(e)}")
        else:
            messages.success(request,"Post Updated successfully")
            return redirect("/blog/")
    blog=Blog.objects.get(pk=id) 
    return render(request,"post.html",{"post":blog})

def upload_file(request):
    if request.method=="POST":
        # form = UploadFile(request.POST,request.FILES)
        # print(form)
        file=request.FILES["file"]
        mymodel=Mymodel(file=file)
        mymodel.save()
        return HttpResponse(str(file))
    else:
        form=UploadFile()

    return render(request,"file.html",{"form":form})
