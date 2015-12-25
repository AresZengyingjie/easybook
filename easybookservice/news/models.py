from django.db import models
from django.contrib import admin
# Create your models here.


class news(models.Model):
	class Meta:
		verbose_name = 'news'
		verbose_name_plural = verbose_name
	newsid  = models.CharField('id',max_length=10)
	title          = models.CharField('title',max_length=30)
	url   =   models.CharField('url',max_length=100)
	article       = models.TextField ('article',blank=True,max_length=2000)
	def __unicode__(self):
		return str(self.title)
  
class newsIssue(admin.ModelAdmin):
	list_display = ('newsid','title','url','article')
  
admin.site.register(news,newsIssue)	