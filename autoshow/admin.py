from django.contrib import admin
from users.models import DesirableAuto


class AutoAdmin(admin.ModelAdmin):
    list_display = ("mark", "model", "price")


admin.site.register(DesirableAuto, AutoAdmin)
