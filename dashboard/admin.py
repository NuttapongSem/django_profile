from django.contrib import admin
from dashboard.models import Skill


# Register your models here.
# admin.site.register(Skill)
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name_skill', 'date_created', 'date_updated']
