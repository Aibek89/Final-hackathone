from django.core.mail import send_mail
from django.template.loader import render_to_string

from post.models import Post
from social_net.celery import app


@app.task
def send_post_info(name):
    # text = f'Hello world {name}!'
    html_message1 = render_to_string('send_mail.html', {'name': name})

    for user in Post.objects.all():
        send_mail(
            'from social_net project',
            '',
            'aibekemil.8989@gmail.com',
            [user.email],
            html_message=html_message1,
        )
