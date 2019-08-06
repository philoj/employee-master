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
    template_name = 'apps/employees/login.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/employees/home.html'


class AddEmployeeView(RequireAdminAccessMixin, ModelFormMixin, TemplateView):
    template_name = 'apps/employees/employee-add.html'


class EmployeeList(RequireAdminAccessMixin, ListView):
    template_name = 'apps/employees/employee-list.html'
