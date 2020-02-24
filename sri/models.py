from django.db import models

class Details(models.Model):
    bodytype1=models.CharField(max_length=25)
    weight1=models.CharField(max_length=25)
    education1=models.CharField(max_length=25)
    occupation1=models.CharField(max_length=25)
    eating1=models.CharField(max_length=25)
    drinking1=models.CharField(max_length=25)
    smoking1=models.CharField(max_length=25)
    star1=models.CharField(max_length=25)
    raasi1=models.CharField(max_length=25)
    dob1=models.DateField()
    country1=models.CharField(max_length=25)
    state1=models.CharField(max_length=25)
    city1=models.CharField(max_length=25)
    father1=models.CharField(max_length=25)
    mother1=models.CharField(max_length=25)
    bno1=models.CharField(max_length=25)
    bma1=models.CharField(max_length=25)
    sno1=models.CharField(max_length=25)
    sma1=models.CharField(max_length=25)
    location1=models.CharField(max_length=25)
    contact1=models.CharField(max_length=25)
    mobile1=models.IntegerField()
    ao1=models.CharField(max_length=25)
    def __str__(self):
        return self.dob1