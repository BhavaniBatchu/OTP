from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    
class Aadhar(models.Model):
    name = models.CharField(max_length=32)
    father = models.CharField(max_length=32)
    dob = models.DateField()
    address = models.TextField()
    phone = models.PositiveIntegerField()
    profile = models.ImageField(upload_to="profiles")
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    mail = models.CharField(default="abc@gmail.com")