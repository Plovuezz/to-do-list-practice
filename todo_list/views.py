from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo_list.forms import TaskCreateForm
from todo_list.models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").all()


def do_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect(reverse("list:task-list"))


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("list:task-list")
    form_class = TaskCreateForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("list:task-list")
    form_class = TaskCreateForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")

