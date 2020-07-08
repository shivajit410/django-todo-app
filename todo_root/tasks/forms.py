from django import forms
from django.forms import ModelForm

from .models import Task


class TaskForm(forms.ModelForm):

    title = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={"placeholder": "Add new task..."})
    )

    class Meta:
        model = Task
        fields = "__all__"

