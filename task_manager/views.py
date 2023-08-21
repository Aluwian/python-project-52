from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = "users/form.html"
    next_page = reverse_lazy("Home")
    success_message = "You are logged in"
    extra_context = {"title": "Log in", "button_text": "Log in"}


class LogoutUserView(LogoutView):
    next_page = reverse_lazy("Home")
