from django.db import models




class State(models.Model):
    message  =   models.CharField(max_length=30)
    symbol   =   models.ImageField(blank=True,upload_to='system')  


