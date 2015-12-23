from django.shortcuts import render
from hospital.models import hospital
from depart.models import depart
from prof.models import prof
from users.models import users
from doctor.models import doctor
from django.shortcuts import render_to_response
# Create your views here.
	
def searchDep(request,username):
	depList = depart.objects.all()
	profList = prof.objects.all()
	docList = doctor.objects.all()
	user = users.objects.get(username = username)
	return render_to_response('searchDep.html',{'depList':depList,'profList':profList,'docList':docList,'user':user})
	
def searchDep1(request,depid,username):
	user = users.objects.get(username = username)
	depList = depart.objects.all()
	profList = prof.objects.all()
	dep = depart.objects.get(departid = depid)
	docList = dep.doctor_set.all()
	return render_to_response('searchDep.html',{'depList':depList,'profList':profList,'docList':docList,'user':user})
	
def searchDep2(request,proid,username):
	user = users.objects.get(username = username)
	depList = depart.objects.all()
	profList = prof.objects.all()
	pro = prof.objects.get(profid = proid)
	docList = doctor.objects.filter(prof = pro.profName)
	return render_to_response('searchDep.html',{'depList':depList,'profList':profList,'docList':docList,'user':user})