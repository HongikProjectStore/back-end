from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
    # overwriting
    def create_superuser(self, phonenumber, password=None):
        user = self.model(
            phonenumber=phonenumber
        )
        user.is_admin = True
        print(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

# Create your models here.
class MyUsers(AbstractUser) :
    name = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 6)
    age = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile/', default='default.png')
    num_go_to_store = models.IntegerField(default=2)
    time_to_go_to_store = models.IntegerField(default=3)

@receiver(post_save, sender=MyUsers)
def create_user_profile(sender, instance,created, **kwargs):
    if created:
        MyUsers.objects.create(user=instance)
