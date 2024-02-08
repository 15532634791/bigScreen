from django.urls import path, re_path, include
from rest_framework import routers
from .views import Login, Register
router = routers.DefaultRouter()

urlpatterns = [
    re_path('login/', Login.as_view()),   # 登录功能验证
    re_path('register/', Register.as_view()),
    # path('users/<int:pk>/', UserView.as_view(
    #     {"get": "retrieve", "delete": "destroy", "post": "update"}
    # )),

]