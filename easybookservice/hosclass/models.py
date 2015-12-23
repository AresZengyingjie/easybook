from django.db import models
from django.contrib import admin
# Create your models here.


class hosclass(models.Model):
	class Meta:
		verbose_name = 'hosclass'
		verbose_name_plural = verbose_name
	hosclassid  = models.CharField('id',max_length=10)
	hosclass          = models.CharField('hosclass',max_length=10)
  
class hosclassIssue(admin.ModelAdmin):
	list_display = ('hosclassid','hosclass') 
admin.site.register(hosclass,hosclassIssue)	