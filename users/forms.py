from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class StyleFormMixin:
    """Формы с красивым стилем"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class DateInput(forms.DateInput):
    """Форма выбора даты"""
    input_type = 'date'

    def __init__(self, attrs=None):
        super().__init__(attrs={'type': 'date'})


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """Форма профиля"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'birth_date', 'avatar', 'phone')
        widgets = {
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'дд.мм.гггг'},
                                                 years=range(2024, 1924, -1)),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
