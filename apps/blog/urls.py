from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_blog'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('new/', views.new_post, name='new_post'),
]