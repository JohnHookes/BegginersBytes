from . import views
from django.urls import path
from .views import post_detail

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name="post_detail"),
]