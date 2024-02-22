from django.contrib import admin
# from django.contrib.admin.models import LogEntry
from blog.models import Blog
from blog.models import Mymodel
# admin.site.register(LogEntry)
admin.site.register(Blog)
# Register your models here.
admin.site.register(Mymodel)
