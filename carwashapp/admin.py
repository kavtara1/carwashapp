from django.contrib import admin

from carwashapp.models import CompanyName, Employee, Branches


@admin.register(CompanyName)
class CompanyNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'personal_number']
    list_display = ['__str__', 'personal_number']


@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    search_fields = ['city', 'location']
    list_display = ['__str__', 'number_of_boxes']
