from django.contrib import admin

from django.contrib import admin
from .models import User
from .models import Test

admin.site.register(User)
admin.site.register(Test)

