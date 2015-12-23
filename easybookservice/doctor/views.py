from django.shortcuts import render
from hospital.models import hospital
from depart.models import depart
from prof.models import prof
from users.models import users
from doctor.models import doctor
from django.shortcuts import render_to_response
# Create your views here.
	
def doctorInfor(request,docid,username):
	doc = doctor.objects.get(doctorid = docid)
	user = users.objects.get(username = username)
	hos = doc.hos
	return render_to_response('doctorInfor.html',{'doc':doc,'hos':hos,'user':user})
	


# Create your views here.
