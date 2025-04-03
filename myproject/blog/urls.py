from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 블로그 홈 페이지로 연결
]
from django.urls import path
from . import views  # 같은 폴더의 views.py를 불러옴

urlpatterns = [
    path("create/", views.create, name="create"),  # 여기 등록!
]

from django.urls import path
from . import views  # 같은 앱 내의 views 가져오기

urlpatterns = [
    path("create/", views.create, name="create"),  # create 뷰 연결
]

