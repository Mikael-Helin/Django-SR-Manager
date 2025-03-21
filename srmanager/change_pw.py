import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'srmanager.settings')
django.setup()

# Now it's safe to import Django models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def change_password(username):
    try:
        user = User.objects.get(username=username)
        new_password = get_random_string(length=40)
        user.set_password(new_password)
        user.save()
        print(f"Password for '{username}' changed successfully.")
        print(f"New password: {new_password}")
    except User.DoesNotExist:
        print(f"User '{username}' not found!")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python change_pw.py <username>")
    else:
        change_password(sys.argv[1])
