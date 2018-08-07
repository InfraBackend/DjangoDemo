from django.db import models

from django_fsm import FSMField,transition

# Create your models here.

class UserProfile(models.Model):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    score = models.IntegerField(null=True, verbose_name='成绩')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class ReviewStatus(models.Model):
    """回访状态"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField(max_length=20, verbose_name='状态名称')
    class Meta:
        verbose_name = "回访状态"
        verbose_name_plural = verbose_name
class StatusOption(models.Model):
    """状态选项"""
    status = models.ForeignKey(ReviewStatus, on_delete=models.CASCADE, verbose_name='状态')
    value = models.CharField(max_length=20, verbose_name='状态值')
    class Meta:
        verbose_name = "状态选项"
        verbose_name_plural = verbose_name

