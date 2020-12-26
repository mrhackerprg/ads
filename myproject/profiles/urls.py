from . import views
from django.urls.conf import path

urlpatterns = [
    path('' , views.home , name="home"),
    path('index_red/' , views.red , name='index_red'),
    path('index_blue/' , views.blue , name='index_blue'),
    path('fatemeh/' , views.green , name='index_green'),
    path('index_gothic/' , views.gothic , name='index_gothic'),
    path('index_yellow/' , views.yellow , name='index_yellow'),
    path('index_android/' , views.android , name='index_android'),
    
]