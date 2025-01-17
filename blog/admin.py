from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(AuthorProfile)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title", )}
  list_display = ['slug', 'published_at']

admin.site.register(Post, PostAdmin)