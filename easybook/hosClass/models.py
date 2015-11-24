from django.db import models
from django.contrib import admin
# Create your models here.


class hosClass(models.Model):
	class Meta:
		verbose_name = 'hosClass'
		verbose_name_plural = verbose_name
	hosClassid  = models.CharField('id',max_length=10)
	hosClass          = models.CharField('hosClass',max_length=10)
  
class hosClassIssue(admin.ModelAdmin):
	list_display = ('hosClassid','hosClass') 
admin.site.register(hosClass,hosClassIssue)	