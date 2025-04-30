from django.urls import path
from account import views as v1

urlpatterns = [
    path('register/', v1.register, name ="register"),
    path('login/' , v1.login_view , name ="login"),
    path('home/' , v1.home , name ='home'),
    path('logout/', v1.logout_view , name= "logout"),




]