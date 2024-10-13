from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    roll_no=models.IntegerField()
    reg_no=models.CharField(max_length=30,null=True)
    full_name=models.CharField(max_length=30)
    birth_date=models.DateField()
    gender=models.CharField(max_length=10)
    father_name=models.CharField(max_length=30)
    mother_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phone_no=models.IntegerField()
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
