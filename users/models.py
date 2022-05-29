from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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
    image = models.IntegerField(default=1)
    num_go_to_store = models.IntegerField(default=2)
    time_to_go_to_store = models.IntegerField(default=3)
