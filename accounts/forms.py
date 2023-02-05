from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        field_order = ['first_name', 'last_name', 'email', 'password','mobile_phone','home_phone','adress','zip_code','city','country','kbis']
        exclude = ['groups','is_staff','is_admin','is_active','is_superuser','user_permissions','username','date_joined','last_login']
