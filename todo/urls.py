from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskEditView



app_name = 'todo'

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('<int:pk>/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/edit/', TaskEditView.as_view(), name='edit_task'),
]