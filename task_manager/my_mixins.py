from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class CustomLoginRequiresMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.ERROR,
                _("You are not authorized! Please sign in."),
            )
            return redirect(reverse_lazy("Login"))
        return super().dispatch(request, *args, **kwargs)


class CustomPermissionRequiredMixin(UserPassesTestMixin):
    permission_message = None
    permission_url = None

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)
