from django.contrib import admin
from .models import Book, Comment


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    ordering = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'text')
    ordering = ('book', 'user')


admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
