from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
# one to many relationship
class ChaiReview(models.Model):
    chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.chai.name}'
    

# Many to many relationship