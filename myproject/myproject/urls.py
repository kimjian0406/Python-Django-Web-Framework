"""
URL configuration for myproject project.

from django.contrib import admin
from django.urls import path
from blog import views 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", views.create, name="create"),  # 이거 꼭 있어야 함!
]

from django.contrib import admin
from django.urls import path, include  # include 추가!
from blog import views  # blog 앱 임포트!

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # blog 앱의 URLConf 포함!
]

from django.urls import path
from . import views  # 같은 앱 내의 views 가져오기

urlpatterns = [
    path("create/", views.create, name="create"),  # create 뷰 연결
]

