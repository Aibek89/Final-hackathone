from django.core.mail import send_mail


def send_confirmation_email(code, email):
    full_link = f'http://localhost:8000/account/active/{code}'
    send_mail(
        'from social_net project',
        full_link,
        'aibekemil.8989@gmail.com',
        [email]
    )


def forgot_password_email(code, email):
    send_mail(
        'Восстановление пароля',
        f'Ваш код подтверждения: {code}',
        'aibekemil.8989@gmail.com',
        [email]
    )