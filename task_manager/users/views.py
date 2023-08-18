from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


class UsersListView(TemplateView):
    template_name = "users/users_list.html"
    users = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
