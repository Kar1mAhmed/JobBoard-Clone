from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, null=True, blank=True)

    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self) -> str:
        return self.user.__str__()
    
    
    
class City(models.Model):
    name = models.CharField(max_length=20)
    

    def __str__(self) -> str:
        return str(self.name)