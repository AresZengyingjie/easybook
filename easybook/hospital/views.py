from django.shortcuts import render
from hospital.models import hospital
from hosClass.models import hosClass
from hosType.models import hosType
from depart.models import depart
from prof.models import prof
from users.models import users
from doctor.models import doctor
from advice.models import advice
from django.shortcuts import render_to_response
# Create your views here.
	
def searchHosp(request,username):
	hosList = hospital.objects.all()
	hosCList = hosClass.objects.all()
	hosTList = hosType.objects.all()
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
	docList = doctor.objects.filter(hos_id = hos.hospitalid, dep_id = dep.departid)	
	return render_to_response('hospitalInfor.html',{'hos':hos,'depList':depList,'profList':profList,'docList':docList,'user':user,'adviceList':adviceList})
	
def selectdoc2(request,hosptalid,profid,username):
	user = users.objects.get(username = username)
	hos = hospital.objects.get(hospitalid = hosptalid)
	adviceList = hos.advice_set.all()
	profList = prof.objects.all()
	depList = hos.depart_set.all()
	prof = prof.objects.get(profid = profid)
	docList = doctor.objects.filter(prof = prof,hos_id = hos.hospitalid)
	return render_to_response('hospitalInfor.html',{'hos':hos,'depList':depList,'profList':profList,'docList':docList,'user':user,'adviceList':adviceList})
   
def selecthosp1(request,hostypeid,username):
	user = users.objects.get(username = username)
	hosTList = hosType.objects.all()
	hosCList = hosClass.objects.all()
	hosT = hosType.objects.get(hosTypeid = hostypeid)
	hosList = hospital.objects.filter(level = hosT.hosType)
	return render_to_response('searchHosp.html',{'hosList':hosList,\
    'hosTList':hosTList,'hosCList':hosCList,'user':user})
    
def selecthosp2(request,hosclassid,username):
	user = users.objects.get(username = username)
	hosTList = hosType.objects.all()
	hosCList = hosClass.objects.all()
	hosC = hosClass.objects.get(hosClassid = hosclassid)
	hosList = hospital.objects.filter(classes = hosC.hosClass)
	return render_to_response('searchHosp.html',{'hosList':hosList,\
    'hosTList':hosTList,'hosCList':hosCList,'user':user})