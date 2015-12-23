from django.db import models
from django.contrib import admin
from users.models import users
from doctor.models import doctor

# Create your models here.
  
class books(models.Model):
	class Meta:
		verbose_name = 'books'
		verbose_name_plural = verbose_name
	user = models.ForeignKey(users)
	doc = models.ForeignKey(doctor)
	hospital         = models.CharField('hospital',max_length=20)
	depart           = models.CharField ('depart',max_length=10)
	docprof        = models.CharField ('docprof',max_length=10)
	hosAddr          = models.CharField('hosAddr',max_length=40)
	time            = models.CharField('time',max_length=10)
	patientName          = models.CharField('patientName',max_length=10)
	patientID          = models.CharField('patientID',max_length=20)
	tel           = models.CharField('tel',max_length=50)
	bookID           = models.CharField ('bookID',max_length=500)
	
	def __unicode__(self):
		return self.bookID
  
class booksIssue(admin.ModelAdmin):
	list_display = ('user','doc','hospital','depart','docprof','hosAddr','time','patientName','patientID','tel','bookID')
	
admin.site.register(books,booksIssue)
		
