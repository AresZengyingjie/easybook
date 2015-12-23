from django.db import models
from django.contrib import admin
from hospital.models import hospital
from depart.models import depart

# Create your models here.
  
class doctor(models.Model):
	class Meta:
		verbose_name = 'doctor'
		verbose_name_plural = verbose_name
	hos = models.ForeignKey(hospital) 
	dep = models.ForeignKey(depart)
	doctorid  = models.CharField('id',max_length=10)
	docname          = models.CharField('docname',max_length=10)
	docmail   =  models.EmailField('Email',unique = True)
	prof         = models.CharField('prof',max_length=20)
	hosp          = models.CharField ('hosp',max_length=30)
	depa          = models.CharField('depa',max_length=20)
	goodat            = models.TextField('goodat',blank=True,max_length=100)
	time          = models.CharField('time',max_length=15)
	exp          = models.TextField('exp',blank=True,max_length=500)
	
	
	def __unicode__(self):
		return self.docname
  
class docIssue(admin.ModelAdmin):
	list_display = ('doctorid','docname','docmail','prof','hosp','depa','goodat','time','exp')
	
admin.site.register(doctor,docIssue)
		
