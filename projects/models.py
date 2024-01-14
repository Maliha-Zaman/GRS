
from django.db import models
import hashlib

class Test(models.Model):
    input_text = models.CharField(max_length=255)
    output_text = models.CharField(max_length=255)
    match = models.BooleanField(default=False)
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)  # Add this line for the reset token
    tests = models.ManyToManyField(Test, blank=True)  # Add this line for the array of objects

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()
