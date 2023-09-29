from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.utils.translation import gettext_lazy as _


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = "layout/form.html"
    next_page = reverse_lazy("home")
    success_message = _("You are logged in")
    extra_context = {"title": _("Log in"), "button_text": _("Enter")}


class LogoutUserView(LogoutView):
    next_page = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _("You are logged out"))
        return response
