from django.contrib import admin

# Register your models here.



from .models import User,Task,Blog

# Register your models here.

admin.site.register(User)

admin.site.register(Task)

admin.site.register(Blog)