from django.urls import path

from apps.employees.views import HomeView, LoginView, EmployeeList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('add', EmployeeList.as_view(), name='employee-add'),
    path('employees', EmployeeList.as_view(), name='employees-list'),
]
