#장고 프로젝트 전체의 API 담당. URL들 담당
# 사용자가 어떤 주소로 접근할 수 있게 정해주는 공간
"""mySpartaSns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views # 지금 내가 있는파일에서 view.py를 가져올거야!

urlpatterns = [
    path('admin/', admin.site.urls),
    # test라는 url로 views.py의 base_response함수와 연결시켜줌
    path('test/', views.base_response, name='first_test'),
    # first라는 url로 views.py의 first_view함수와 연결시켜줌
    path('first/', views.first_view, name='first_view'),
    #include('user앱의 urls.py'와) mySpartaSns의 urls.py가 연결되었다.
    path('',include('user.urls')), #이렇게 해줘야 user에서작성한 urls.py도 장고가 이해함
    path('',include('tweet.urls')),
]
