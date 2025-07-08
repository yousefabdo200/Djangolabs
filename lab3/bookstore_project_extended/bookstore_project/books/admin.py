from django.contrib import admin
from .models import Book, Category, ISBN

class ISBNInline(admin.StackedInline):
    model = ISBN
    max_num = 1
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'views', 'user')
    list_filter = ('categories', 'user')
    search_fields = ('title',)

admin.site.register(Category)
admin.site.register(ISBN)
