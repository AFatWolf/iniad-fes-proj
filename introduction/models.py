from django.db import models

# Create your models here.
class ClubMembers(models.Model):
    name = models.TextField()
    year = models.TextField()
    course = models.TextField()
    description = models.TextField()    
    githubAccount = models.TextField()
    atcoderAccount = models.TextField()





