from django.urls import path
from myapp import views #이걸 해야 views에 있는걸 보여준다
import random

urlpatterns = [
    path('', views.index),
    # 루트가 아무것도 없는곳으로 접속했을때 
    path('create/', views.create),
    # create로 접속했을때
    path('read/<id>/', views.read),  #view.에 함수명을 적어주면 그대로 나온다
    #<>안에 있는건 언제든지 바꿀수 있다고 표시한것
    path('test/', views.test)
]
