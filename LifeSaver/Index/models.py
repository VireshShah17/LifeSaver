from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length = 300)
    email = models.EmailField()
    phone_num = models.CharField(max_length = 10)
    address = models.TextField()
    city = models.CharField(max_length = 300)
    state = models.CharField(max_length = 300)
    bloodgroup = models.CharField(max_length = 5)
    identityproof = models.ImageField(upload_to='photos/')
    birthdate = models.DateField()
    gender = models.CharField(max_length = 10, choices=[('male', 'Male'), ('female', 'Female')])
    disorder = models.CharField(max_length = 3, choices=[('yes', 'Yes'), ('no', 'No')])
    organs = models.ManyToManyField('Organ', blank=True)

    def __str__(self):
        return self.name


class Organ(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
