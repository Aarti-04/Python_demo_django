from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    '''User'''
    class Meta:
        '''Meta'''
        model=User
        fields="__all__"

class BlogSerializer(serializers.ModelSerializer):
    '''Blog'''
    userid=UserSerializer(many=False)
    class Meta: 
        '''Meta'''
        model=Blog
        fields='__all__'