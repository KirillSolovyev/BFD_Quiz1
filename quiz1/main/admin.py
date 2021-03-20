from django.contrib import admin
from .models import Book, Journal


@admin.register(Book)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'price']
    ordering = ['name']
    list_filter = ['name', 'created_at', 'price']


@admin.register(Journal)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'price']
    ordering = ['name']
    list_filter = ['name', 'created_at', 'price']
