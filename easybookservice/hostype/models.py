from django.db import models
from django.contrib import admin
# Create your models here.


class hostype(models.Model):
	class Meta:
		verbose_name = 'hostype'
		verbose_name_plural = verbose_name
	hostypeid  = models.CharField('id',max_length=10)
	hostype          = models.CharField('hostype',max_length=10)

class hostypeIssue(admin.ModelAdmin):
	list_display = ('hostypeid','hostype')   
admin.site.register(hostype,hostypeIssue)	