from django.contrib import admin
from .models import User, Seeker, Shelter

admin.site.register(User)
admin.site.register(Seeker)
admin.site.register(Shelter)