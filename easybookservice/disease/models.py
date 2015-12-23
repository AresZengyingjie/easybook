from django.db import models
from django.contrib import admin
from depart.models import depart

# Create your models here.
  
class disease(models.Model):
	class Meta:
		verbose_name = 'disease'
		verbose_name_plural = verbose_name
	dep = models.ManyToManyField(depart) 
	diseaseid  = models.CharField('id',max_length=10)
	disename          = models.CharField('disename',max_length=50)
	disenamel         = models.CharField('disenamel',max_length=100)
	diseSym           = models.TextField ('diseSym',blank=True,max_length=300)
	godepart          = models.CharField('godepart',max_length=30)
	spread            = models.CharField('spread',max_length=30)
	position          = models.CharField('position',max_length=50)
	highrisk          = models.CharField('highrisk',max_length=50)
	method           = models.CharField('method',max_length=50)
	intro           = models.TextField ('intro',blank=True,max_length=500)
	
	def __unicode__(self):
		return self.disename
  
class diseIssue(admin.ModelAdmin):
	list_display = ('diseaseid','disename','disenamel','diseSym','godepart','spread','position','highrisk','method','intro')
	
admin.site.register(disease,diseIssue)
		
