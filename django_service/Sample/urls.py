from django.urls import path
from . import views

app_name = 'Sample'

urlpatterns = [
    path('', views.SampleListView.as_view(), name='SampleList'),
]
