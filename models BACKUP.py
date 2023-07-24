from django.db import models

from datetime import datetime

# Create your models here.

class User(models.Model):
    # id=models.CharField(max_length=200)

    Name = models.CharField(max_length=200, null=False)

    Email=models.EmailField(max_length = 254,null=False)

    MobileNumber=models.CharField(max_length=200,null=False)
    
    Password=models.CharField(max_length=10)

    Address=models.TextField(max_length=200)

    def __str__(self):
        return self.Name
    

class Task(models.Model):
    id=models.BigAutoField(auto_created=True, primary_key=True , default=1)

    TaskName = models.CharField(max_length=200)

    Date= models.DateField(default=None )

    Time=models.TimeField(default=None )

    #Assign = models.ForeignKey( User,  on_delete=models.CASCADE, default='')
       
    Assign=models.CharField(max_length=100 , editable=True)

    Status=models.CharField(max_length=100)

    user=models.ForeignKey(User,on_delete=models.CASCADE , default=None )

   # Address=models.TextField()

    def __str__(self):
        return self.TaskName    
