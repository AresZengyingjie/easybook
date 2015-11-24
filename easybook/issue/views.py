from django.shortcuts import render
from hospital.models import hospital
from disease.models import disease
from doctor.models import doctor
from users.models import users
from prof.models import prof
from depart.models import depart
from news.models import news
from issue.models import issue
from django.shortcuts import render_to_response

def help(request,issid,username):
	user = users.objects.get(username = username)
	if issid == '1':
		return render_to_response('help.html',{'user':user})
	if issid =='2':
		return render_to_response('contact.html',{'user':user})
	if issid =='3':
		return render_to_response('connect.html',{'user':user})
	if issid =='4':
		return render_to_response('advice.html',{'user':user})