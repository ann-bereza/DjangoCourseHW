import argparse
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoCourseHW.settings')
django.setup()

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


def generate_token(name):
    User = get_user_model()
    try:
        user = User.objects.get(username=name)
        token, created = Token.objects.get_or_create(user=user)
        print(token.key)
    except User.DoesNotExist:
        print(f"User {name} does not exist in the db. Token is not generated")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple CLI to generate and/or print out the auth token for a given username.")
    parser.add_argument("name", type=str, help="User must be registered")
    args = parser.parse_args()

    generate_token(args.name)
