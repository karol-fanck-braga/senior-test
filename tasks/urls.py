from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskListCreate.as_view(), name="task-view-create"),
    path("tasks/<int:pk>/", views.TaskRetrieveUpdateDestroy.as_view(), name="update")
]