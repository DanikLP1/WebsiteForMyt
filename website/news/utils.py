from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from website.settings import TEMPLATES_DIRS, EMAIL_HOST_USER
import os

def get_client_ip(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip

def send_contact_email_message(subject, email, content, ip, user_id):
    
    if user_id:
        user = User.objects.get(id=user_id)
    else:
        user = None
    message = render_to_string(os.path.join(TEMPLATES_DIRS, 'contact_mail.html'),  {
        'email': email,
        'content': content,
        'ip': ip,
        'user': user
    })

    email = EmailMessage(subject, message, EMAIL_HOST_USER, ['danik.lp2016@yandex.ru', 'alina.popova2004@gmail.com'])
    return email.send(fail_silently=False)
