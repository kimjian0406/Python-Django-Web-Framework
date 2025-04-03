from django.contrib import admin
from django.urls import path, include  # include 추가!
from blog import views  # blog 앱 임포트!

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # blog 앱의 URLConf 포함!
]

