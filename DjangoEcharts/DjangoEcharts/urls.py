"""
URL configuration for DjangoEcharts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('user/', include('Apps.Login.urls')),
    re_path('screen/', include('Apps.BigScreen.urls')),
    re_path('docs/', include_docs_urls(
        title='接口文档',
        authentication_classes=[],
        permission_classes=[AllowAny],
    )),
]
