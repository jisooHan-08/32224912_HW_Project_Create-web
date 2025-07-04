"""
URL configuration for hw_project_buildweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from vote_evalu_project import views


urlpatterns = [
    path('admin/', admin.site.urls),   # 장고 관리자 페이지
    path('', views.home, name='home'),   # 프로젝트 시작 페이지 - 각종 페이지 연결 버튼 
    path('project/create/', views.create_project, name='create_project'),   # 프로젝트 생성
    path('project/success/', views.project_success, name='project_success'),   # 생성 완료 페이지
    path('projects/', views.project_list, name='project_list'),  # 프로젝트 리스트 URL
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),  # 특정 ID(pk)를 가진 프로젝트의 상세 페이지를 보여주는 URL 패턴
    path('projects/sorted/', views.sorted_project_list, name='sorted_project_list'), # 평균 점수 순으로 정렬된 프로젝트 목록

   

]
