from django.db import models

class newsuser(models.Model):
    userName=models.CharField(max_length=100) 
    email=models.CharField(max_length=100)
    userPhone=models.IntegerField(max_length=100)
    userGender=models.charField(max_length=1) 