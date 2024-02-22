from django.http import JsonResponse
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import BlogSerializer,UserSerializer
from blog.models import Blog
from django.core.cache import cache
import time

@api_view(['GET'])
def getRoutes(request):
    '''View Routes'''
    routes=[
        {'GET':'/api/blog'},
        {'GET':'/api/blog/id'},
        {'POST':'/api/blog/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
        {'POST':'/api/blog'},
        {'PATCH':'/api/update/<int:id>'},
        {'DELETE':'/api/delete/<int:id>'}]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlogs(request):
    '''View Blogs'''
    payload=[]
    db=None
    if cache.get('blogs'):
        start=time.time()
        blogs=cache.get('blogs')
        db="reddis"
        serializer=BlogSerializer(blogs,many=True)
        print("from cache")
        print(f"total time {time.time()-start}")
        return Response(serializer.data)
    else:
        start=time.time()
        blogs = Blog.objects.all()
        # print(blogs)
        serializer=BlogSerializer(blogs,many=True)
        cache.set('blogs',blogs)
        db="sqlite"
        print("from sqlite")
        print(f"total time {time.time()-start}")
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlog(request,id):
    '''View Single Blog'''
    blog = Blog.objects.get(id=id)
    serializer=BlogSerializer(blog,many=False)
    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    '''Create Blog'''
    data = request.data
    user= request.user
    data["userid"]=user
    blog,created= Blog.objects.get_or_create(**data)
    blog.save()  
    print(blog)
    return Response(BlogSerializer(blog,many=False).data)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_post(request,pk):
    '''Update Blog'''
    data=Blog.objects.get(pk=pk)
    to_update_data=request.data
    for key,value in to_update_data.items():
        if hasattr(data,key):
            setattr(data,key,value)
    data.save()
    return Response(BlogSerializer(data,many=False).data)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,pk):
    '''Delete Blog''' 
    try:
        data=Blog.objects.get(pk=pk)
        data.delete()
    except Blog.DoesNotExist:
        return Response("Blog not found",status=status.HTTP_404_NOT_FOUND)
    return Response({"deleted":True})

    