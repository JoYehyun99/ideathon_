from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICE = (('W','여성'),('M','남성'))
SLEEP_HABIT_CHOICE = (('A','A'),('B','B'),('C','C'),)
SLEEP_TIME_CHOICE = (('D','D'),('E','E'),('F','F'),)
CLEAN_CHOICE = (('G','G'),('H','H'),('I','I'),)
COOK_CHOICE = (('J','J'),('K','K'),('L','L'),)
BUDGET_CHOICE = (('M','M'),('N','N'),('O','O'),)

class UserInfo(AbstractUser):
    profile_img = models.ImageField(upload_to ="common/", blank=True, null =True)
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE,default='W')
    age = models.IntegerField(default=0)
    school = models.CharField(max_length=30)
    major = models.CharField(max_length=50)
    studentID =models.IntegerField(default=0)
    sleep_habit = models.CharField(max_length=10,choices=SLEEP_HABIT_CHOICE,default='A')
    sleep_time = models.CharField(max_length=10,choices=SLEEP_TIME_CHOICE,default='D')
    cleanliness = models.CharField(max_length=10,choices=CLEAN_CHOICE,default='G')
    cook = models.CharField(max_length=10,choices=COOK_CHOICE,default='J')
    smoke =  models.BooleanField(default=False)
    budget = models.CharField(max_length=10,choices=BUDGET_CHOICE,default='M')
    hope_area = models.CharField(max_length=50)
    introduction = models.TextField()
    profile_active = models.BooleanField(default=True)
