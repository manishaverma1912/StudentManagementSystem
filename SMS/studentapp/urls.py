from django.urls import path 
from studentapp import views

urlpatterns = [
    path('' , views.index ,name ='index'),
    path('hello/', views.hello , name ="hello"),
    path('test/' , views.test , name = 'test'),
    path('hlo/' , views.hlo , name ="hlo"),
    path('test1/' , views.test1 , name = 'test1'),

]
