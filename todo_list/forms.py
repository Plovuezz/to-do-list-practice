from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from todo_list.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple(),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline < timezone.now():
            raise ValidationError("You can't set a date in the past")
        return deadline