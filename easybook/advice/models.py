from django.db import models
from django.contrib import admin
from users.models import users
from hospital.models import hospital
# Create your models here.

class advice(models.Model):
	class Meta:
		verbose_name = 'advice'
		verbose_name_plural = verbose_name
	user = models.ForeignKey(users)
	hos = models.ForeignKey(hospital)
	recommend = models.CharField('dep',max_length=10)
	treatmentEffect = models.CharField('dep',max_length=10)
	disease = models.CharField('disease',max_length=30)
	doctor = models.CharField('doctor',max_length=10)
	docAttitude = models.CharField('dep',max_length=10)
	dep = models.CharField('dep',max_length=10)
	context = models.CharField('context',max_length = 300)
	
	tel = models.CharField('tel',max_length = 50)

class adviceIssue(admin.ModelAdmin):
	list_display = ('user','hos','dep','context','tel')
	
admin.site.register(advice,adviceIssue)	