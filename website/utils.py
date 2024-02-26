import random
from django.core.mail import send_mail

def generate_four_random_numbers():
    return str(random.randint(1000,9999))

def send_raw_email(subject: str, message: str, sender: str, recipients:list):
    send_mail(subject, message, sender, recipients)
