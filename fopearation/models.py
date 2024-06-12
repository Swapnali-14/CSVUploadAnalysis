from django.db import models

# Create your models here.
class FileOperation(models.Model):
    name=models.CharField(max_length=255)
    csv_file = models.FileField(null=True)


