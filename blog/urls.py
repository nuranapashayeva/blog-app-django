from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('add_post/', views.add_post, name='add_post'),
]
