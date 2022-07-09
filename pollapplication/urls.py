
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first, name='first'),
    path('create/', views.create, name='create'),
    path('results/<poll_id>/	', views.results, name='results'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('login/', views.login, name='login'),
    path('logincode/', views.logincode, name='logincode'),
    path('register/', views.register, name='register'),
    path('registercode/', views.registercode, name='registercode'),
]
 