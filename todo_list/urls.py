from django.urls import path
from todo_list.views import (TaskListView, do_task, TaskCreateView,
                             TaskUpdateView, TaskDeleteView, TagListView, TagCreateView, TagUpdateView, TagDeleteView)

app_name = "list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/do-task/<int:pk>/", do_task, name="do-task"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]