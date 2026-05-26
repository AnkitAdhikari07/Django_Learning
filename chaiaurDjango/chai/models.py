from django.db import models
from django.utils import timezone

class chaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'Masala'),
        ('GR', 'Ginger'),
        ('KL', 'Kiwi'),
        ('CH', 'Chocolate'),
        ('EL', 'Elaichi'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')

    def __str__(self):
        return self.name