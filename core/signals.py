# signals.py
import requests
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

def get_ip_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        print(response)
        data = response.json()
        print(data)
        return data.get("city", "Unknown location")
    except:
        return "Unknown location"

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    # Capture platform information
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    platform = user_agent

    # Capture IP and location
    ip_address = request.META.get('REMOTE_ADDR')
    location = get_ip_location(ip_address)

    # Prepare email content
    subject = 'Login Notification'
    message = f"""
    Hello {user.username},

    You just logged in with the following details:
    - Platform: {platform}
    - Location: {location}

    If this was not you, please contact support immediately.
    """
    
    # Send email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
