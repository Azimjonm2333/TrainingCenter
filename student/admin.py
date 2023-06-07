from django.contrib import admin
from student.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ["fullname", 'email']
    search_fields = ["name"]
    date_hierarchy = "create_time"
