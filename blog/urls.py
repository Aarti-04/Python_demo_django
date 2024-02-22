from django.urls import path
from blog.views import *

urlpatterns = [
    path("",home),
    path("create/",create_post),
    path("update/",create_post),
    path("delete/<int:id>",delete_post),
    path("edit/<int:id>",edit_post),
    path("list/",upload_file)
    # path('upload/', upload_file, name='upload_file'),

]