from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, CreateView

from apps.employees.forms import CreateEmployeeForm
from apps.employees.models import User


class RequireAdminAccessMixin(AccessMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class LoginView(DjangoLoginView):
    template_name = 'apps/employees/login.html'


class LogoutView(DjangoLogoutView):
    http_method_names = ['post']


class AddEmployeeView(RequireAdminAccessMixin, CreateView):
    http_method_names = ['get', 'post']
    template_name = 'apps/employees/employee-add.html'
    model = User
    object = None
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('home')

    def post(self, *args, **kwargs):
        add_employee_form = self.get_form()
        if add_employee_form.is_valid():
            return self.form_valid(add_employee_form)
        else:
            return self.form_invalid(add_employee_form)


class EmployeeListView(LoginRequiredMixin, ListView):
    template_name = 'apps/employees/employee-list.html'
    model = User


class EditEmployeeView(AccessMixin, UpdateView):
    http_method_names = ['get', 'post']
    template_name = 'apps/employees/employee-edit.html'
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'phone', 'address',)
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and (self.request.user.is_admin or self.request.user == self.get_object()):
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()
