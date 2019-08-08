from django.contrib.auth.forms import UserCreationForm

from apps.employees.models import User


class CreateEmployeeForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'phone', 'address', )