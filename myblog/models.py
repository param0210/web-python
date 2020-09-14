from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
GENDER=(
    ('male','MALE'),
    ('female','FEMALE'),
    ('transgender','TRANSGENDER')
    )

class MyUser(AbstractUser):
    first_name=models.CharField(max_length=100,null=False,blank=False)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=100,choices=GENDER,null=True,blank=True)
    mobile_number=models.CharField(max_length=100,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    age=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.username

    # def age(self):
    #     dob=self.date_of_birth
    #     current_date=datetime.today()
    #     return((current_date.year-dob.year)-(current_date.month,current_date.day)<(dob.month,dob.day))

     
    class Meta:
        verbose_name_plural='Users'

class Blog(models.Model):
    title=models.CharField(max_length=100,blank=True)
    description=models.TextField()
    slug=models.SlugField()
    created_on=models.DateTimeField(auto_now_add=True)
    created_time=models.TimeField()
    writen_by=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    thumbnail=models.ImageField(default='default.png',blank=True)
    
    class Meta:
        managed=True
        verbose_name_plural='Blogs'

    def __str__(self):
        return self.title
    
    def snnippet(self):
        return self.description[:60]+"...."