
from django.contrib import admin
from django.urls import path,include
from pollapplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pollapplication.urls')),
    path('home/',include('pollapplication.urls')),
    path('create/',include('pollapplication.urls')),
    path('result/',include('pollapplication.urls')),
    path('vote/',include('pollapplication.urls')),
    path('login/',include('pollapplication.urls')),
    path('logincode/',include('pollapplication.urls')),
    path('register/',include('pollapplication.urls')),
    path('registercode/',include('pollapplication.urls')),
]
