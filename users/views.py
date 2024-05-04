from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView
from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.services import send_new_password


class LoginView(BaseLoginView):
    """Страница входа"""
    template_name = 'users/login.html'


def logout_view(request):
    """Страница выхода"""
    logout(request)
    return redirect(reverse_lazy('users:login'))


class RegisterView(CreateView):
    """Страница регистрации"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Сохраняем нового пользователя"""
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.save()

        """Отправляем письмо с подтверждением регистрации"""
        token = default_token_generator.make_token(new_user)
        new_user.email_confirmation_token = token
        new_user.save()

        # Генерация URL для подтверждения регистрации
        confirmation_url = self.request.build_absolute_uri(
            reverse('users:confirm_registration', kwargs={'token': token}))

        # Создание HTML-содержимого письма
        message = render_to_string('users/confirmation_email.html', {
            'user': new_user,
            'confirmation_url': confirmation_url,
        })

        # Отправка письма
        send_mail(
            subject='Подтверждение регистрации',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            html_message=message
        )

        messages.info(self.request, 'Письмо с подтверждением регистрации отправлено на вашу почту.')
        return redirect(self.success_url)


def confirm_registration(request, token):
    """Страница подтверждения регистрации"""
    try:
        user = User.objects.get(email_confirmation_token=token)
        # Проверяем токен
        if default_token_generator.check_token(user, token):
            # Если токен верен, устанавливаем флаг активности пользователя как True
            user.is_active = True
            user.save()
            messages.success(request, 'Ваша почта подтверждена! Можете войти в свой профиль.')
            return redirect('users:login')
        else:
            messages.error(request, 'Недействительный токен подтверждения.')
            return redirect('users:invalid_token')
    except User.DoesNotExist:
        messages.error(request, 'Пользователь с таким токеном подтверждения не найден.')
        return redirect('users:invalid_token')


def invalid_token_view(request):
    """Страница недействительного токена"""
    return render(request, 'users/invalid_token.html')


class ProfileView(LoginRequiredMixin, UpdateView):
    """Страница профиля"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    """Страница генерации пароля"""
    new_password = User.objects.make_random_password()
    request.user.set_password(new_password)
    request.user.save()
    send_new_password(request.user.email, new_password)
    return redirect(reverse('medical_services:home'))


def reset_password(request):
    """Страница смены пароля"""
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            user.save()
            send_mail(
                subject='Восстановление пароля',
                message=f'Для входа используйте новый пароль: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            return render(request, 'users/password_recovery_success.html')
        except User.DoesNotExist:
            return render(request, 'users/password_recovery_failure.html')
    else:
        return render(request, 'users/reset_password.html')
