from django.contrib import admin
from .models import BigScreen
from .models import UploadFile
from .models import InstallMaintainScore
from .models import InternetQualityScore

admin.site.register(BigScreen)
admin.site.register(UploadFile)
admin.site.register(InstallMaintainScore)
admin.site.register(InternetQualityScore)
