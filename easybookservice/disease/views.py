from django.shortcuts import render
from django.shortcuts import render_to_response
from disease.models import disease
from depart.models import depart
from doctor.models import doctor
from users.models import users
# Create your views here.

def diseInfor(request,diseid,username):
	dise = disease.objects.get(diseaseid = diseid)
	depList = dise.dep.all()
	for depa in depList:
		docList = depa.doctor_set.all()
	user = users.objects.get(username = username)
	return render_to_response('diseaseInfor.html',{'dise':dise,'user':user,'docList':docList})