from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User #user là một model có sẵn
from django.core.validators import MaxValueValidator,MinValueValidator #là cách để kiểm tra giá trị 
# Create your models here.

class ProductPortfolio(models.Model):
    STATUS = (
        ("D","In Development"),
        ("P","Planned"),
        ("F","Finished"),
        ("S","Suspensed"),
        )
    title = models.CharField(max_length = 144,null = False,blank = False,
                             unique = True,default = "")
    status = models.CharField(max_length = 144,default = "Finished", 
                             choices = STATUS)
    description = models.CharField(max_length = 144,blank = False,
                             unique = True,default = "")
    content = models.ImageField(upload_to = "product_pics/",blank = True)
    class Meta():
        indexes = [models.Index(fields = ('title',))]
    def __str__(self):
        return self.title

class Profile(models.Model):
    LANG = (
        ("en","English"),
        ("vi","Vietnam"),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lang = models.CharField(max_length = 3,choices = LANG)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    intro = models.CharField(max_length = 144)
    class Meta():
        unique_together = (('user','lang'),)
        index_together = (('user','lang'),)
    def __str__(self):
        return f"{self.user.username}'s Profile" 