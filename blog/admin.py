from django.contrib import admin

# Register your models here.
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'owner')
    # list_display_links = ('title', 'publish', 'author')
    list_filter = ('publish', 'owner')
    search_fields = ('title', 'body')
    raw_id_fields = ('owner', )
    date_hierarchy = ('publish')
    ordering = ('publish', 'owner')
    actions_on_bottom = True
    actions_selection_counter = True


admin.site.site_header = '博客管理系统'
admin.site.site_title = '博客管理系统'

admin.site.register(Blog, BlogAdmin)
