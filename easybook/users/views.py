from django.shortcuts import render
from hospital.models import hospital
from hosClass.models import hosClass
from hosType.models import hosType
from prof.models import prof
from users.models import users
from doctor.models import doctor
from books.models import books
from django.shortcuts import render_to_response

def addbook(request,docid,username):
	patientname = request.GET.get('patient-name','')
	idcard = request.GET.get('id-card','')
	phone = request.GET.get('phone','')
	doc = doctor.objects.get(doctorid = docid)
	docprof = doc.prof
	user = users.objects.get(username = username)
	hos = doc.hos
	dep = doc.dep
	user.books_set.create(doc_id = doc.doctorid, hospital = hos.name,depart = dep.departName,docprof= doc.prof,hosAddr = hos.address, time = "sat", patientName =patientname, patientID = idcard,tel = hos.telephone,bookID = '1')
	bookList = user.books_set.all()
	return render_to_response('error.html')

def mybook(request,username):
	user = users.objects.get(username = username)
	bookList = user.books_set.all()
	return render_to_response('mybook.html',{'bookList':bookList,'user':user})            

def visitForm(request,docid,username):
	user = users.objects.get(username = username)
	doc = doctor.objects.get(doctorid = docid)
	hos = doc.hos
	return render_to_response('visitForm.html',{'doc':doc,'hos':hos,'user':user})