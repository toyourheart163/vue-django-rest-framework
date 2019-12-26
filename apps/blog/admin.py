from django.contrib import admin

from .models import Blog, Comment, Tag, Category

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'owner', 'created']
    fields = ['title', 'body', 'category', 'tags']
    inlines = [CommentInline]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'user', 'created']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Blog, BlogAdmin)
