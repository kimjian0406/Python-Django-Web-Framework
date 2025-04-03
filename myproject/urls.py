# myproject/urls.py

from django.contrib import admin
from django.urls import path, include  # include를 추가합니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # blog 앱의 urls.py를 포함시킵니다.
]

from django.urls import path
from blog import views  # 'myapp'이 아니라 'blog'로 수정!

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", views.create, name="create"),  # 추가!
]
