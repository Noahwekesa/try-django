from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
from django.conf import settings


class TryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        try:
            is_strong = validate_password(settings.SECRET_KEY)
        except Exception as e:
            msg = f"Weak secret key {e.messsages}"
            self.fail(msg)
