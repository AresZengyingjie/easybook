from django.db import models
from django.contrib import admin
# Create your models here.


class prof(models.Model):
	class Meta:
		verbose_name = 'prof'
		verbose_name_plural = verbose_name
	profid  = models.CharField('id',max_length=10)
	profName          = models.CharField('profName',max_length=10)
	def __unicode__(self):
		return str(self.profName)

class profIssue(admin.ModelAdmin):
	list_display = ('profid','profName')   
admin.site.register(prof,profIssue)	