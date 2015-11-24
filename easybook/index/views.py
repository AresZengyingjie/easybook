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
# Create your views here.

def index(request):
	hosList = hospital.objects.all()
	diseList = disease.objects.all()
	docList = doctor.objects.all()
	newList = news.objects.all()
	return render_to_response('index.html',{'hosList':hosList,'diseList':diseList,'docList':docList,'newList':newList})
	
def login(request):
	return render_to_response('login.html')
	
def register(request):
	return render_to_response('register.html')
	
def addUser(request):
	username = request.GET.get('username','')
	password = request.GET.get('password','')
	email = request.GET.get('email','')
	users.objects.create(username = username, password = password, email = email)
	return render_to_response('login.html',{'username':username})
	
def checkLogin(request):
	hosList = hospital.objects.all()
	diseList = disease.objects.all()
	docList = doctor.objects.all()
	newList = news.objects.all()
	username = request.GET.get('username','')
	password = request.GET.get('password','')
	userList = users.objects.filter(username = username)
	for user in userList:
		if user.password == password:
			return render_to_response('index_login.html',{'hosList':hosList,'diseList':diseList,'docList':docList,'newList':newList,'user':user})
	return render_to_response('error.html')
 
def helpIssue(request,username):
	issueList = issue.objects.all()
	user = users.objects.get(username = username)
	return render_to_response('help.html',{'user':user})
	
# def issue(request,issid):
	# issueList = issues.objects.all()
	# iss = issues.objects.get(issueid = issid)
	# return render_to_response('issue.html',{'issueList':issueList,'iss':iss})
    
def search(request,username):
	user = users.objects.get(username = username)
	text = request.GET.get('key','')
	profList = prof.objects.all()
	hosList = hospital.objects.filter(name = text)
	diseList = disease.objects.filter(disename = text)
	depList = depart.objects.filter(departName = text)
	docList = doctor.objects.filter(docname = text)
	if hosList:
		for hos in hosList:
			if hos.name == text:
				depList = hos.depart_set.all()
				return render_to_response('hospitalInfor.html',{'hos':hos,'depList':depList,'profList':profList,'user':user})
	elif diseList:
		for dise in diseList:
			if dise.disename == text:
				return render_to_response('diseaseInfor.html',{'dise':dise,'user':user})
	elif depList:
		for dep in depList:
			if dep.departName == text:
				docList = dep.doctor_set.all()
				return render_to_response('searchDep.html',{'depList':depList,'profList':profList,'docList':docList,'user':user})
	elif docList:
		for doc in docList:
			if doc.docname == text:
				return render_to_response('doctorInfor.html',{'doc':doc,'user':user})
	else:
		return render_to_response('error.html')
	
    


	
