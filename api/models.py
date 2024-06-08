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

class Content(models.Model):
    LANG = (
        ("en","en-US"),
        ("vi","vi-VN"),
        ("de","de-DE")
        )
    title = models.CharField(max_length = 144,default = "",unique = True)
    lang = models.CharField(max_length = 6,choices = LANG)
    welcome_word = models.CharField(max_length = 200,default = "Welcome to")
    intro_word = models.CharField(max_length = 200, default = 
                                  "Your one stop site for every engineering")
    learnmore_button = models.CharField(max_length = 30,default = "Learn more")
    login_word = models.CharField(max_length = 30,default = "Login")
    username_word = models.CharField(max_length = 30,default = "Username")
    password_word = models.CharField(max_length = 30,default = "Password")
    toggleRegister_word = models.CharField(max_length = 200,
                        default = "You don't have an account? Register here!")
    toggleLogin_word = models.CharField(max_length = 200,
                        default = "You already have an account? Login here!")
    about_word = models.CharField(max_length = 400, default = 
                        "Our mission is about simplify engineering project")
    class Meta():
        indexes = [models.Index(fields = ('lang',))]
    def __str__(self):
        return self.title