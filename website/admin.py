from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import UserEmailVerification

User = get_user_model()



# Model List
class UserEmailVerificationAdmin(admin.ModelAdmin):
    list_display = ["user", "code"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["email"]

# # Register models
admin.site.register(User, UserAdmin)
admin.site.register(UserEmailVerification, UserEmailVerificationAdmin)

# # Unregister Group
admin.site.unregister(Group)

