from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from api import views
urlpatterns = [
    # path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.getRoutes),
    path('blog/',views.getBlogs),
    path('blog/<int:id>',views.getBlog),
    path('blog/create',views.create_post),
    path('blog/update/<int:pk>',views.update_post),
    path('blog/delete/<int:pk>',views.delete_post)

]
