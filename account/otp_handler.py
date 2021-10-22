from random import randint
from .models import User
from datetime import datetime
def create_otp():
    return randint(1000,9999)

def send_otp(email,otp):
    print("OTP = {}".format(otp))

def check_otp_expiration(email):
    try:
        user = User.objects.get(email=email)
        now = datetime.now()
        otp_time = user.otp_create_time
        if (now - otp_time).seconds >120:
            return False
        return True
    except User.DoesNotExist:
        return False

def check_change_password_time_expiration(email):
    try:
        user = User.objects.get(email=email)
        now = datetime.now()
        otp_time = user.otp_create_time
        if (now - otp_time).seconds >300:
            return False
        return True
    except User.DoesNotExist:
        return False