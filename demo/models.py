from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=38, default="Title")
    STAR = (
        ('1','*'), 
        ('2','* *'),
        ('3','* * *'),
        ('4','* * * *'),
        ('5','* * * * *')
    )
    stars = models.CharField(choices=STAR, max_length=35)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0,  max_digits=3, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)