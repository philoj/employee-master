from django.urls import path

from apps.employees.views import LoginView, EmployeeListView, AddEmployeeView, LogoutView, EditEmployeeView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('add', AddEmployeeView.as_view(), name='employee-add'),
    path('edit/<int:pk>/', EditEmployeeView.as_view(), name='employee-edit'),
    path('', EmployeeListView.as_view(), name='home'),
]
