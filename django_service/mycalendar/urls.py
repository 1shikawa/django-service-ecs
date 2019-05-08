from django.urls import path, include
from . import views
from accounts.forms import ContactForm
from django.views.generic.base import TemplateView
# from accounts.forms import ContactForm
from django.contrib.auth import views as auth_views  # ログアウトに必要

app_name = 'mycalendar'

urlpatterns = [
    path(
        'month_with_schedule/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'month_with_schedule/<int:year>/<int:month>/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'month_with_schedule/<int:year>/<int:month>/<int:day>',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    # 複数登録
    path(
        'month_with_schedule/NewMultiAdd/<int:year>/<int:month>/<int:day>',
        views.NewMultiAdd.as_view(), name='NewMultiAdd'
    ),
    path(
        'month_with_schedule/NewMultiEdit/<int:year>/<int:month>/<int:day>',
        views.NewMultiEdit.as_view(), name='NewMultiEdit'
    ),
    # 入力一覧
    path(
        'DailyInputList/', views.DailyInputList.as_view(), name='DailyInputList'
    ),

    # 日次集計
    path(
        'DailySumList/', views.DailySumList.as_view(), name='DailySumList'
    ),

    # 月次集計
    path(
        'MonthlySumList/', views.MonthlySumList.as_view(), name='MonthlySumList'
    ),
    # CSVエクスポート
    path(
        'SumExport/', views.SumExport, name='SumExport'
    ),
    # チャート
    path(
        'Chart/', views.Chart.as_view(), name='Chart'
    ),
    # 個別グラフ
    path(
        'Graph/', views.Graph.as_view(), name='Graph'
    ),
    # お問い合わせ
    path(
        'contact/', views.Contact(ContactForm), name='contact'
    ),

]
