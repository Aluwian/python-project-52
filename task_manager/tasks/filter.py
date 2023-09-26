import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Task
from task_manager.labels.models import Label


class FilterTasks(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())
    author_task = django_filters.BooleanFilter(
        label=_("Only own tasks"),
        widget=forms.CheckboxInput,
        method="is_user_author",
    )

    def is_user_author(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ["status", "executor"]
