from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # path('linux/', views.all_blogs, name='all_blogs'),
    # path('aster/', views.all_blogs, name='all_blogs'),
]
