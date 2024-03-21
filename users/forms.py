from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import CheckboxInput

from users.models import User


class StyleFormMixin:
    """Миксин для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2') # 2 пароля


class UserForm(StyleFormMixin, UserChangeForm):
    """Форма редактирования профиля"""
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'avatar', 'phone', 'country')

    def __init__(self, *args, **kwargs):
        """Спрячем пароль"""
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
