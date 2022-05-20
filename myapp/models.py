from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


 #Create your models here.
class User(AbstractUser):
    choic = (
      ('male','Male'),
       ('female','Female'),
    )
    ROLE = (

        ('admin', 'Admin'),
        ('hr', 'HR'),
    )
    roles = models.CharField(choices=ROLE,max_length=70,default='hr')
    gender  = models.CharField(choices=choic,max_length=7)
    companyname = models.CharField(max_length=50,null=True,blank=True) 
    
    def __str__(self):
        return self.username+' '+self.roles 

class JobPost(models.Model):
    SALARY =(
        ('03-05lakh','03-05lakh'),
        ('06-09lakh','06-09lakh'),
        ('10-12lakh','10-12lakh'),
        ('12&Abovelakh','12&Abovelakh'),
    )

    state_choices = (("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry"))

    EXPERIENCE =(
        ('FRESHER','FRESHER'),
        ('02-04 YEAR','02-04 YEAR'),
        ('05&Above','05&Above'),
    )
    CATEGORY=(
        ('IT','IT'),
        ('ENGINEERING','ENGINEERING'),
        ('RESEARCH','RESEARCH'),
        ('MARKETING','MARKETING'),
        ('SALES','SALES'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(choices=state_choices, max_length=150)
    salary = models.CharField(choices=SALARY,max_length=45)
    position = models.CharField(max_length=200)
    vacancy = models.IntegerField()
    category = models.CharField(choices=CATEGORY,max_length=50)
    experience = models.CharField(choices=EXPERIENCE,max_length=17)
    description = models.CharField(max_length=200,null=True,blank=True)
 
class CandidateProfile(models.Model):
    choice = (
      ('male','Male'),
       ('female','Female'),
    )
    name = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(choices=choice,max_length=8)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    resume = models.FileField(upload_to='profile/')
    company = models.ForeignKey(JobPost,on_delete=models.CASCADE,null=True,blank=True)
    
