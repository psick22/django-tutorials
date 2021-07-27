from django.db import models


class Book(models.Model):
    STATUS = (
        (0, 'Unknown'), (1, 'processed'), (2, 'paid')
    )
    title = models.CharField(blank=False, unique=True, max_length=36)
    status = models.IntegerField(default=0, choices=STATUS)
    description = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    published = models.DateTimeField(null=True, default=None)
    cover = models.FileField(upload_to='covers/', blank=True)
    is_published = models.BooleanField(default=False)
