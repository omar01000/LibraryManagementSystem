from django.contrib import admin
from .models import Book,Category

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['total_rental']
    list_display = ['title', 'status', 'price', 'rental_price_day', 'rental_period', 'total_rental']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']