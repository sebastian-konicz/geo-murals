from django.db import models
from django.utils import timezone

# Create your models here.
class Mural(models.Model):
    editor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    painter = models.CharField(max_length=100)
    street = models.CharField(max_length=200)

    lon = models.DecimalField(decimal_places=12,max_digits=15)
    lat = models.DecimalField(decimal_places=12,max_digits=15)

    type = models.CharField(max_length=50)
    # creation_date = models.DateField()
    #
    photo_url = models.URLField()
    photo = models.ImageField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title