from django.db import models

# Create your models here.
class Car(models.Model):  
    Brand=models.CharField(max_length=30)
    Type=models.CharField(max_length=20)
    Seats=models.CharField(max_length=2)
    Image=models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.Brand
    
    
    
class Booking(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    Phoneno=models.CharField(max_length=10)
    boarding=models.CharField(max_length=30)
    drop=models.CharField(max_length=30)
    date_of_travel=models.DateField()
    car=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=10)
    
    def __str__(self):
        return self.username