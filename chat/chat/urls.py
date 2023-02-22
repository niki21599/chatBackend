"""chat URL Configuration

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
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from chatBackend.views import testHtml, register, get_chats, get_messages, get_users_without_chat, post_chat, post_message, get_users,get_user_id, get_last_message, create_guest_chats


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", obtain_auth_token), 
    path("test/", testHtml), 
    path("register/", register), 
    path("chat/add", post_chat), 
    path("chat/get", get_chats),
    path("message/add", post_message),
    path("message/get", get_messages),
    path("users/add", get_users_without_chat),
    path("users/get", get_users),
    path("message/get/last", get_last_message),
    path("user_id/get", get_user_id), 
    path("guestchat/add", create_guest_chats)

]
