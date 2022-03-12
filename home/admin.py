from django.contrib import admin

from home.models import User
from home.models import Contact

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
