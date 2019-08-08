from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import ModelFormMixin

from apps.employees.forms import CreateEmployeeForm
from apps.employees.models import User


class RequireAdminAccessMixin(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionError


class LoginView(DjangoLoginView):
    template_name = 'apps/employees/login.html'


class LogoutView(DjangoLogoutView):
    http_method_names = ['post']


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/employees/home.html'


class AddEmployeeView(RequireAdminAccessMixin, ModelFormMixin, TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'apps/employees/employee-add.html'
    model = User
    form_class = CreateEmployeeForm
    object = None
    success_url = reverse_lazy('employees-list')

    def post(self, *args, **kwargs):
        add_employee_form = self.get_form()
        if add_employee_form.is_valid():
            return self.form_valid(add_employee_form)
        else:
            return self.form_invalid(add_employee_form)


class EmployeeList(RequireAdminAccessMixin, ListView):
    template_name = 'apps/employees/employee-list.html'
    model = User
