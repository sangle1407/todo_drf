from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.apiOverview,name='api_overview'),
    path('task_list/',views.taskList,name='task_list'),
    path('task_detail/<str:pk>/',views.taskDetail,name='task_detail'),
    path('task_create/',views.taskCreate,name='task_create'),
    path('task_update/<str:pk>/',views.taskUpdate,name='task_update'),
    path('task_delete/<str:pk>/',views.taskDelete,name='task_delete'),
]
