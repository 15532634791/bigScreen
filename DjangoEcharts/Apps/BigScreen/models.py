from django.db import models


class UploadFile(models.Model):
    file = models.FileField(upload_to='static/uploads')
    created_at = models.DateTimeField(auto_now_add=True)  # 自动设置为对象创建时间

    class Meta:
        db_table = 'uploads'
        verbose_name = '上传文件'
        verbose_name_plural = '上传文件'


class BigScreen(models.Model):
    """
    数据库字段
    """
    id = models.AutoField(primary_key=True)
    county = models.CharField(max_length=150, help_text="区县", null=True, blank=True)
    grid = models.CharField(max_length=150, help_text="网格", null=True, blank=True)
    residential_quarters = models.CharField(max_length=350, help_text="小区", null=True, blank=True)
    zone_of_responsibility = models.CharField(max_length=350, help_text="责任区", null=True, blank=True)
    packaging_and_maintenance = models.CharField(max_length=350, help_text="包保装维", null=True, blank=True)
    userid = models.CharField(max_length=50, help_text="用户账号", null=True, blank=True)
    userid_status = models.CharField(max_length=50, help_text="用户账号状态", null=True, blank=True)
    internet_quality_rating = models.CharField(max_length=50, help_text="上网质量评分", null=True, blank=True)
    scoring_by_install_and_maintain_services = models.CharField(max_length=150, help_text="装维服务评分", null=True, blank=True)
    comprehensive_score = models.DecimalField(help_text="综合得分", null=True, blank=True, max_digits=5, decimal_places=2)

    class Meta:
        db_table = "screen"
        verbose_name = '大屏'
        verbose_name_plural = '大屏'


class InstallMaintainScore(models.Model):
    """
    装维服务评分
    """
    userid = models.CharField(max_length=50, help_text="用户账号", null=True, blank=True)
    score = models.CharField(max_length=150, help_text="装维服务评分", null=True, blank=True)

    class Meta:
        db_table = "install"
        verbose_name = '装维服务'
        verbose_name_plural = '装维服务'


class InternetQualityScore(models.Model):
    """
    上网质量评分
    """
    userid = models.CharField(max_length=50, help_text="用户账号", null=True, blank=True)
    score = models.CharField(max_length=150, help_text="上网质量评分", null=True, blank=True)

    class Meta:
        db_table = "internet"
        verbose_name = '上网质量'
        verbose_name_plural = '上网质量'


