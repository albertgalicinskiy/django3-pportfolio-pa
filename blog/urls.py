from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # path('linux/', views.all_blogs, name='all_blogs'),
    # path('aster/', views.all_blogs, name='all_blogs'),

    # '<int:blog_id>/' - сюда будет приходить запрос из чисел и будет искать id
    # числа в БД через функцию detail в views.py
    path('<int:blog_id>/', views.detail, name='detail')
]
