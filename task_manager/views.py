from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.utils.translation import gettext_lazy as _


class HomePageView(TemplateView):
    template_name = "index.html"


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = "layout/form.html"
    success_message = _("You are logged in")
    extra_context = {"title": _("Log in"), "button_text": _("Enter")}


class LogoutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _("You are logged out"))
        return response
