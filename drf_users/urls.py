"""drf_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from users.views import CustomUserViewSet
# from project.views import ProjectViewSet
# from project.views import ToDOViewSet

from users.views import UserRetrieveAPIView, UserListAPIView
# from project.views import ProjectViewSet

router = DefaultRouter()
# router.register('users', CustomUserViewSet)
# router.register('project', ProjectViewSet)
# router.register('todo', ToDOViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # url for CustomUser
    path('generic/retrive/<int:pk>', UserRetrieveAPIView.as_view()),
    path('generic/list/', UserListAPIView.as_view()),


]
