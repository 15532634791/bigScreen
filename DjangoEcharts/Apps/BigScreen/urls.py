from django.urls import re_path
from .views import BigScreenView
from .views import InstallAndMaintainPersonnelSatisfaction
from .views import InternetQualitySatisfaction
from .views import InternetQualityProportion
from .views import InstallAndMaintainProportion
from .views import CountySatisfaction
from .views import UploadFileViewSet
from .views import GridSatisfaction
from .views import ResponsibilityZoneSatisfaction
from .views import GridRank
from .views import CountyRank
from .views import ResponsibilityZoneRank

from rest_framework import routers
router = routers.DefaultRouter()
# 获取整体接口列表
router.register('list', BigScreenView, basename='big_screen')
# 上传文件接口
router.register(r'upload', UploadFileViewSet, basename='uploads')

urlpatterns = [

    # 装维人员满意度打分
    re_path('score/install/maintain/', InstallAndMaintainPersonnelSatisfaction.as_view()),
    # 上网质量满意度打分
    re_path('score/internet/quality/', InternetQualitySatisfaction.as_view()),
    # 上网质量占比
    re_path('proportion/internet/quality/', InternetQualityProportion.as_view()),
    # 装维占比
    re_path('proportion/install/maintain/', InstallAndMaintainProportion.as_view()),
    # 区县满意度
    re_path('satisfaction/county/', CountySatisfaction.as_view()),
    # 网格满意度
    re_path('satisfaction/grid/', GridSatisfaction.as_view()),
    # 责任区满意度
    re_path('satisfaction/zone/', ResponsibilityZoneSatisfaction.as_view()),
    # 网格排名
    re_path('rank/grid/', GridRank.as_view()),
    # 区县排名
    re_path('rank/county/', CountyRank.as_view()),
    re_path('rank/zone/', ResponsibilityZoneRank.as_view()),
]

urlpatterns += router.urls
