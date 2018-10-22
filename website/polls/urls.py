from django.urls import path
from . import views
# 参考文档 https://docs.djangoproject.com/en/2.1/intro/tutorial02/#database-setup
urlpatterns = [
    path('',views.index, name ='index'),
]