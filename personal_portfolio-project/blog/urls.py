from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('<int:blog_id>/',views.detail,name='detail'),
    path('', views.all_blog, name = 'all_blog'),
]
