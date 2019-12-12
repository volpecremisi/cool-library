from django.contrib import admin

# Register your models here.

from .models import Book, Loan


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',  {'fields': ['title']}),
        ('Author', {'fields': ['author']}),
    ]
    list_display = ['title','author']

admin.site.register(Book, BookAdmin)
admin.site.register(Loan)
