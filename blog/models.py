from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

class Blog(models.Model):
    '''Blog'''
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)

'''Django signals'''
@receiver(post_save,sender=Blog)
def call_blog_api(sender,instance,**kwargs):
    print("Blog is created")
    print(sender,instance,kwargs)
class Mymodel(models.Model):
    file=models.FileField(upload_to="media/uploads/",max_length=250,null=True,default=None)