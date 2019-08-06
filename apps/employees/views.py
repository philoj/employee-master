from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from django.views.generic.edit import ModelFormMixin


class RequireAdminAccessMixin(LoginRequiredMixin, View):
    pass


class LoginView(DjangoLoginView):
    pass


class HomeView(LoginRequiredMixin, TemplateView):
    pass


class AddEmployeeView(RequireAdminAccessMixin, ModelFormMixin, TemplateView):
    pass


class EmployeeList(RequireAdminAccessMixin, TemplateResponseMixin, ContextMixin, ListView):
    pass
