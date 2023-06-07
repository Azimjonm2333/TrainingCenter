from django.contrib import admin
from course.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ["title", "duration"]
    search_fields = ["title"]
    date_hierarchy = "create_time"
