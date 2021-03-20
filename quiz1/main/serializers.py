from rest_framework import serializers
from .models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'price', 'description', 'num_pages', 'genre')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('name', 'price', 'description', 'type', 'publisher')
