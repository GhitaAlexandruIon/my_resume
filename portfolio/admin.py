from django.contrib import admin
from portfolio.models import Project, Technology, Skill


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('title', 'description')


admin.site.register(Project, ProjectAdmin)

admin.site.register(Technology)
admin.site.register(Skill)
