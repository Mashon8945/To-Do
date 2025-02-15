from django.urls import path

from .views import home, remove

url_patterns = [
    path('', home, name='todo'),
    path('del/<str:item_id>/', remove, name='del'),
]