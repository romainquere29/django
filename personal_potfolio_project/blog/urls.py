from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_blogs, name='home_blogs'),
    path('<int:blog_id>/', views.details, name='details'),
]