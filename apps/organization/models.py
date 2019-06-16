from datetime import datetime

from django.db import models


# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市")
    desc = models.CharField(max_length=200, verbose_name="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    """
    课程机构
    """
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述", blank=True, null=True)
    location = models.CharField(max_length=50, verbose_name="通讯详细地址")
    has_auth = models.BooleanField(default=False, verbose_name="是否已经认证")
    index = models.IntegerField(default=9999, verbose_name="排序")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="机构封面图")
    address = models.CharField(max_length=150, verbose_name="机构地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    city = models.ForeignKey(CityDict, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name="教师名字")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="公司名称")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击量")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏次数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
