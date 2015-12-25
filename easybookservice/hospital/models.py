from django.db import models
from django.contrib import admin

# Create your models here.
class hospital(models.Model):
    class Meta:
        verbose_name = 'hospital'
        verbose_name_plural = verbose_name
    hospitalid  = models.CharField('id',max_length=10)
    name          = models.CharField('name',max_length=50)
    level         = models.CharField('level',max_length=10)
    quality           = models.CharField('quality',max_length=10)
    classes           = models.CharField('classes',max_length=10)
    insurance          = models.CharField('insurance',max_length=10)
    telephone           = models.CharField('telephone',max_length=20,blank=True)
    address       = models.CharField('address',max_length=200,blank=True)
    docnum      =    models.CharField('docnum',max_length=10)
    patientnum   = models.CharField('patientnum',max_length=10)
    service         = models.CharField('service',max_length=60,blank=True)
    summary        = models.TextField ('summary',blank=True,max_length=2000)
    def __unicode__(self):
        return str(self.name)
	
	
class hosIssue(admin.ModelAdmin):
	list_display = ('hospitalid','name','level','quality','classes','insurance','telephone','address','docnum','service','summary')
	
	
		
admin.site.register(hospital,hosIssue)