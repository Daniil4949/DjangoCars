from django.contrib import admin
from users.models import Customer, Provider, AutoShow, UserCar


class AdminCustomer(admin.ModelAdmin):
    list_display = ("name",)


class AdminUserCar(admin.ModelAdmin):
    list_display = ("role",)


class AdminAutoShow(admin.ModelAdmin):
    list_display = ("name",)


class AdminProvider(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Customer, AdminCustomer)
admin.site.register(AutoShow, AdminAutoShow)
admin.site.register(UserCar, AdminUserCar)
admin.site.register(Provider, AdminProvider)
