from django.db import models
from django.contrib import admin
from hospital.models import hospital
# Create your models here.

class depart(models.Model):
	class Meta:
		verbose_name = 'depart'
		verbose_name_plural = verbose_name
	hos = models.ManyToManyField(hospital)
	departid  = models.CharField('departid',max_length=10)
	departName          = models.CharField('departName',max_length=50)
	def __unicode__(self):
		return self.departName

class departIssue(admin.ModelAdmin):
	list_display = ('departid','departName')		
admin.site.register(depart,departIssue)	