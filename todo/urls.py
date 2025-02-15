from django.urls import path

from .views import home, remove

urlpatterns = [
    path('todo/', home, name='todo'), 
    path('del/<str:item_id>/', remove, name='del'),
]