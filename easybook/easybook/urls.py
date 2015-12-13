"""easybook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'index.views.index'),
	url(r'^login/$', 'index.views.login'),
	url(r'^register/$', 'index.views.register'),
	url(r'^addUser/$', 'index.views.addUser'),
	url(r'^helpIssue/(?P<username>\w*)/$', 'index.views.helpIssue'),
	url(r'^help/(?P<issid>\d*)/(?P<username>\w*)/$', 'issue.views.help'),
	url(r'^search_result/(?P<username>\w*)/$', 'index.views.search'),
	url(r'^visitForm/(?P<docid>\d*)/(?P<username>\w*)/$', 'users.views.visitForm'),
	url(r'^addbook/(?P<docid>\d*)/(?P<username>\w*)/$', 'users.views.addbook'),
	url(r'^deletebook/(?P<bookid>\d*)/(?P<username>\w*)/$', 'books.views.deletebook'),
	url(r'^mybook/(?P<username>\w*)/$', 'users.views.mybook'),
	url(r'^addadvice/(?P<username>\w*)/$', 'advice.views.addadvice'),
	url(r'^deleteadvice/(?P<tel>\d*)/(?P<username>\w*)/$', 'advice.views.deleteadvice'),
	url(r'^updateadvice/(?P<tel>\d*)/(?P<username>\w*)/$', 'advice.views.updateadvice'),
	url(r'^myadvice/(?P<username>\w*)/$', 'advice.views.myadvice'),
	url(r'^checkLogin/$', 'index.views.checkLogin'),
	url(r'^index_loginagain/(?P<username>\w*)/$', 'index.views.index_again'),
	url(r'^hospitalInfor/(?P<hosptalid>\d*)/(?P<username>\w*)/$', 'hospital.views.hospitalInfor'),
	url(r'^hospitalInfor/(?P<hosptalid>\d*)/(?P<depid>\d*)/(?P<username>\w*)/$', 'hospital.views.selectdoc1'),
	url(r'^hospitalInfor/(?P<hosptalid>\d*)/(?P<profid>\d*)/(?P<username>\w*)/$', 'hospital.views.selectdoc2'),
	url(r'^doctorInfor/(?P<docid>\d*)/(?P<username>\w*)/$', 'doctor.views.doctorInfor'),
	url(r'^searchHosp/(?P<username>\w*)/$', 'hospital.views.searchHosp'),
	url(r'^searchDep/(?P<username>\w*)/$', 'depart.views.searchDep'),
	url(r'^searchDep1/(?P<depid>\d*)/(?P<username>\w*)/$', 'depart.views.searchDep1'),
	url(r'^searchDep2/(?P<proid>\d*)/(?P<username>\w*)/$', 'depart.views.searchDep2'),
	url(r'^selecthosp1/(?P<hostypeid>\d*)/(?P<username>\w*)/$', 'hospital.views.selecthosp1'),
	url(r'^selecthosp2/(?P<hosclassid>\d*)/(?P<username>\w*)/$', 'hospital.views.selecthosp2'),
	url(r'^diseInfor/(?P<diseid>\d*)/(?P<username>\w*)/$', 'disease.views.diseInfor'),
]
