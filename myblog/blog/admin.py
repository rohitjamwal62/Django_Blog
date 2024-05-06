from django.contrib import admin
from .models import Blog, Comment, Like, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'created_at')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Tag, TagAdmin)
