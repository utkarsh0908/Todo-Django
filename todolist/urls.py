from django.contrib import admin
from django.urls import path
from.views import *


urlpatterns = [
    path('',TaskListView.as_view(),name='home'),
    path('delete/<int:id>',delete_task,name='delete'),
    path('add',add_task,name='add_task'),
    path('update/<int:id>',update_status,name='update'),

]
