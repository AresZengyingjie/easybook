from django.shortcuts import render
from hospital.models import hospital
from hosclass.models import hosclass
from hostype.models import hostype
from depart.models import depart
from prof.models import prof
from users.models import users
from doctor.models import doctor
from advice.models import advice
from django.shortcuts import render_to_response
import random
# Create your views here.
	
def searchHosp(request,username):
	hosList = hospital.objects.all()
	hosCList = hosclass.objects.all()
	hosTList = hostype.objects.all() 
	user = users.objects.get(username = username)
	return render_to_response('searchHosp.html',{'hosList':hosList,'hosCList':hosCList,'hosTList':hosTList,'user':user})
 
def hospitalInfor(request,hosptalid,username):
	hosList = hospital.objects.all()
	profList = prof.objects.all()
	user = users.objects.get(username = username)
	for hos in hosList:
		if hos.hospitalid == hosptalid:
			docList = hos.doctor_set.all()
			depList = hos.depart_set.all() 
			adviceList = hos.advice_set.all()
			return render_to_response('hospitalInfor.html',{'hos':hos,'depList':depList,'profList':profList,'docList':docList,'user':user,'adviceList':adviceList})
			
			
def selectdoc1(request,hosptalid,depid,username):
	user = users.objects.get(username = username)
	hos = hospital.objects.get(hospitalid = hosptalid)
	adviceList = hos.advice_set.all()
	profList = prof.objects.all()
	depList = hos.depart_set.all()
	dep = depart.objects.get(departid = depid)
	docList = doctor.objects.filter(hosp = hos.name, depa = dep.departName)	
	return render_to_response('hospitalInfor.html',{'hos':hos,'depList':depList,'profList':profList,'docList':docList,'user':user,'adviceList':adviceList})
	
def selectdoc2(request,hosptalid,proid,username):
	user = users.objects.get(username = username)
	hos = hospital.objects.get(hospitalid = hosptalid)
	adviceList = hos.advice_set.all()
	profList = prof.objects.all()
	depList = hos.depart_set.all()
	prof1 = prof.objects.get(profid = proid)
	docList = doctor.objects.filter(prof = prof1.profName,hosp = hos.name)
	return render_to_response('hospitalInfor.html',{'hos':hos,'depList':depList,'profList':profList,'docList':docList,'user':user,'adviceList':adviceList,'prof':prof})
   
def selecthosp1(request,hostypeid,username):
	user = users.objects.get(username = username)
	hosTList = hostype.objects.all()
	hosCList = hosclass.objects.all()
	hosT = hostype.objects.get(hostypeid = hostypeid)
	hosList = hospital.objects.filter(level = hosT.hostype)
	return render_to_response('searchHosp.html',{'hosList':hosList,\
    'hosTList':hosTList,'hosCList':hosCList,'user':user})
    
def selecthosp2(request,hosclassid,username):
	user = users.objects.get(username = username)
	hosTList = hostype.objects.all()
	hosCList = hosclass.objects.all()
	hosC = hosclass.objects.get(hosclassid = hosclassid)
	hosList = hospital.objects.filter(classes = hosC.hosclass)
	return render_to_response('searchHosp.html',{'hosList':hosList,\
    'hosTList':hosTList,'hosCList':hosCList,'user':user})