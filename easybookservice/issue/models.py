from django.db import models
from django.contrib import admin
# Create your models here.


class issue(models.Model):
	class Meta:
		verbose_name = 'issue'
		verbose_name_plural = verbose_name
	issueid = models.CharField('issueid',max_length=5)
	issuename = models.CharField('issuename',max_length=10)
	issuecontent = models.TextField('issuecontent',max_length=10000)
	
class issueIssue(admin.ModelAdmin):
	list_display = ('issueid','issuename','issuecontent')   

  
admin.site.register(issue,issueIssue)	

