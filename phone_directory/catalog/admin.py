from django.contrib import admin

from .models import Company, Staffer


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'adress',
        'creator',
        'created'
        )


@admin.register(Staffer)
class StafferAdmin(admin.ModelAdmin):
    list_display = (
        'staffer',
        'post',
        'work_phone',
        'personal_phone',
        'fax_number'
        )
