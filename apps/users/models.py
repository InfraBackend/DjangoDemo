from django.db import models

from django_fsm import FSMField,transition

# Create your models here.


class Role(models.Model):
    """角色"""
    name = models.CharField(max_length=20, verbose_name='角色名称')
    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

class UserProfile(models.Model):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")),                                        default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    score = models.IntegerField(null=True, verbose_name='成绩')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='导入时间')
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL,
                             verbose_name='咨询师')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class Clue(models.Model):

