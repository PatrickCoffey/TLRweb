from django.db import models

# Create your models here.


class user(models.Model):
    """This is a user of the web app"""
    
    
    def __unicode__(self):
        return 