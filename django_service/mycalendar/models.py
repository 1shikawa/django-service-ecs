import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, slug_re
from django.contrib.auth.models import AbstractUser


class LargeItem(models.Model):
    """大項目"""
    name = models.CharField(verbose_name='大項目', max_length=50)

    def __str__(self):
        return self.name


class MiddleItem(models.Model):
    """中項目"""
    name = models.CharField(verbose_name='中項目', max_length=50)
    parent = models.ForeignKey(LargeItem, verbose_name='大項目', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """スケジュール"""
    LargeItem = models.ForeignKey(LargeItem, verbose_name='大項目', on_delete=models.PROTECT)
    MiddleItem = models.ForeignKey(MiddleItem, verbose_name='中項目', on_delete=models.PROTECT)
    SmallItem = models.CharField(verbose_name='小項目', max_length=50, blank=True)
    summary = models.CharField(verbose_name='概要', max_length=50, blank=True)
    description = models.TextField(verbose_name='詳細な説明', blank=True)
    memo = models.CharField(verbose_name='備考', max_length=50, blank=True)
    start_time = models.TimeField(verbose_name='開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField(verbose_name='終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField(verbose_name='日付')
    kosu = models.PositiveIntegerField(verbose_name='時間（分）', blank=True, default=0, validators=[RegexValidator(
        slug_re,
        '時間（分）には半角英数字のみ指定できます。',
        'invalid'
    )])
    totalkosu = models.PositiveIntegerField(verbose_name='総時間（分）', blank=True, default=0)
    register = models.CharField(verbose_name='登録者', max_length=50)
    created_at = models.DateTimeField(verbose_name='登録日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.LargeItem)
