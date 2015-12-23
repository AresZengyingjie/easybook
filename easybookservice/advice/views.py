from django.shortcuts import render
from django.shortcuts import render_to_response
from advice.models import advice
from hospital.models import hospital
from users.models import users

# Create your views here.
def addadvice(request,username):
	user = users.objects.get(username = username)
	hosname = request.GET.get('hos','')
	hos = hospital.objects.get(name = hosname)
	dep = request.GET.get('dep','')
	recommend = request.GET.get('recommend','')
	treatmentEffect = request.GET.get('treatmentEffect','')
	docAttitude = request.GET.get('docAttitude','')
	disease = request.GET.get('disease','')
	doctor = request.GET.get('doctor','')
	context = request.GET.get('context','')
	tel = request.GET.get('tel','')
	user.advice_set.create(hos = hos, dep = dep, recommend = recommend, treatmentEffect = treatmentEffect, docAttitude = docAttitude, disease = disease ,doctor = doctor,context = context, tel = tel)
	return render_to_response('advice_succeed.html',{'user':user})
	
def myadvice(request, username):
	user = users.objects.get(username = username)
	adviceList = user.advice_set.all()
	return render_to_response('myadvice.html',{'adviceList':adviceList,'user':user})
	
def deleteadvice(request, tel, username):
	user = users.objects.get(username = username)
	advice.objects.filter(tel = tel).delete()
	adviceList = user.advice_set.all()
	return render_to_response('myadvice.html',{'adviceList':adviceList,'user':user})
	
def updateadvice(request, tel, username):
	user = users.objects.get(username = username)
	adviced = advice.objects.get(tel = tel)
	advice.objects.get(tel = tel).delete()
	return render_to_response('advice.html',{'user':user,'advice':adviced})
