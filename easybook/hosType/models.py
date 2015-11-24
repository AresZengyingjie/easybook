from django.db import models
from django.contrib import admin
# Create your models here.


class hosType(models.Model):
	class Meta:
		verbose_name = 'hosType'
		verbose_name_plural = verbose_name
	hosTypeid  = models.CharField('id',max_length=10)
	hosType          = models.CharField('hosType',max_length=10)

class hosTypeIssue(admin.ModelAdmin):
	list_display = ('hosTypeid','hosType')   
admin.site.register(hosType,hosTypeIssue)	