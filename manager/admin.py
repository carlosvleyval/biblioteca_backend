from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date", "biography")
    search_fields = ("name",)


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_date", "price", "available")
    search_fields = ("title",)


admin.site.register(Book, BookAdmin)
