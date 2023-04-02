from django.core.mail import send_mail

def send_email(to_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='youremail@gmail.com',
        recipient_list=[to_email],
        fail_silently=False,
    )