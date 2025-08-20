from django.urls import path
from todo_list.views import TaskListView, do_task, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = "list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/do-task/<int:pk>/", do_task, name="do-task"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
]