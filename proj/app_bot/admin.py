from django.contrib import admin

from .models import Chat, User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "birthday"]


class ChatAdmin(admin.ModelAdmin):
    list_display = ["id"]


admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
