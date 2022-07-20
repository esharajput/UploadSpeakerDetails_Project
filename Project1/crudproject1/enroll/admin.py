from django.contrib import admin
from .models import Speaker
# Register your models here.
@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'email', 'password')
