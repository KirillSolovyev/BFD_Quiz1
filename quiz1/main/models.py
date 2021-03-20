from django.db import models

# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    genre = models.CharField(max_length=32)


class Journal(BookJournalBase):
    JOURNAL_TYPES = (
        ('BUL', 'Bullet'),
        ('FOO', 'Food'),
        ('TRA', 'Travel'),
        ('SPO', 'Sport')
    )
    type = models.CharField(max_length=3, default='BUL')
    publisher = models.CharField(max_length=128)
