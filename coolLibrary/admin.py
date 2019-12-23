from django.contrib import admin

# Register your models here.

from .models import Book, Loan, Date


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',  {'fields': ['title']}),
        ('Author', {'fields': ['author']}),
        ('Quantity', {'fields': ['quantity']}),
    ]
    list_display = ['title','author','quantity']

admin.site.register(Book, BookAdmin)
admin.site.register(Loan)
admin.site.register(Date)
