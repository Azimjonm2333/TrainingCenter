from django.contrib import admin
from estimation.models import Estimation


@admin.register(Estimation)
class EstimationAdmin(admin.ModelAdmin):

    list_display = ["student", "course", 'estimation']
    search_fields = ["course", "student"]
    readonly_fields = ['create_time', 'update_time']
    date_hierarchy = "create_time"
