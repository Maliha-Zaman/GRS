# models.py
from django.db import models
import hashlib



class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)
    # tests = models.ManyToManyField('Test', blank=True)

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()
<<<<<<< HEAD
# class Test(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     result = models.TextField()  # Store the test result
#     timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for when the test was taken
# User.test_set = property(lambda u: Test.objects.filter(user=u))
=======

class Test(models.Model):
    input_text = models.TextField()
    output_text = models.TextField()
    match = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'Test {self.id}'
>>>>>>> a07126ad8087025167d95bb234a6f3a92a301e22
