from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    profile_pix = models.ImageField(upload_to='profile',default='https://img.freepik.com/free-vector/smiling-young-man-illustration_1308-174669.jpg')
    def __str__(self):
        return self.fullname
