from django.db import models
from django.contrib.auth.models import User


class comp(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class postjob(models.Model):
    catchoice=[
        ('remote','remote'),
        ('hybrid','hybrid')
        ]
    jobtype=[
        ('parttime','parttime'),
        ('fulltime','fulltime')
        ]
    exp=[
        ('0 - 1' , '0 - 1'),
        ('1 - 2' , '1 - 2'),
        ('2 - 3' , '2 - 3'),
        ('3 - 4' , '3 - 4'),
        ('4 - 5' , '4 - 5'),
        ('5 - 6' , '5 - 6'),
        ('6 - 7' , '6 - 7'),
        ('7 - 8' , '7 - 8'),
    ]

    cname=models.CharField(max_length=30)
    email=models.EmailField()
    jtitle=models.CharField(max_length=50)
    wtype=models.CharField(max_length=30,choices=catchoice)
    expreq=models.CharField(max_length=30,choices=exp)
    jtype=models.CharField(max_length=30,choices=jobtype)



class modelempreg1(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    dob=models.DateField()
    quali=models.CharField(max_length=50)
    phno=models.IntegerField()
    password=models.CharField(max_length=50)

class applymodel(models.Model):
    compnm=models.CharField(max_length=50)
    jobtitle=models.CharField(max_length=50)
    empname=models.CharField(max_length=50)
    empemail=models.EmailField()
    empph=models.IntegerField()
    exp=models.CharField(max_length=100)
    pdf=models.FileField()


