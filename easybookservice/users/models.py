from django.db import models
from django.contrib import admin
# Create your models here.

class users(models.Model):
    class Meta:
        verbose_name = 'users'
        verbose_name_plural = verbose_name
    username          = models.CharField('username',max_length=50,unique=True)
    password           = models.CharField('password',max_length=15)
    email          = models.CharField('email',max_length=30)
    
    def __unicode__(self):
        return self.username
	
class userIssue(admin.ModelAdmin):
	list_display = ('username','password','email')
		
admin.site.register(users,userIssue)
