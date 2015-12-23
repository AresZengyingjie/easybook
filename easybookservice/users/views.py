import smtplib 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEBase import MIMEBase 
from email.MIMEText import MIMEText 
from email import Encoders 
import os

gmail_user = "18346178020@163.com" 
gmail_pwd = "weichenchen02468"


from django.shortcuts import render
from hospital.models import hospital
from hosclass.models import hosclass
from hostype.models import hostype
from prof.models import prof
from users.models import users
from doctor.models import doctor
from books.models import books
from django.shortcuts import render_to_response

def mail(to, subject, text, attach): 
   msg = MIMEMultipart()

   msg['From'] = gmail_user 
   msg['To'] = to 
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   if os.path.exists(attach): 
       part = MIMEBase('application', 'octet-stream') 
       part.set_payload(open(attach, 'rb').read()) 
       Encoders.encode_base64(part) 
       part.add_header('Content-Disposition', 
           'attachment; filename="%s"' % os.path.basename(attach)) 
       msg.attach(part)

   mailServer = smtplib.SMTP("smtp.163.com", 25) 
   mailServer.ehlo() 
   mailServer.starttls() 
   mailServer.ehlo() 
   mailServer.login(gmail_user, gmail_pwd) 
   mailServer.sendmail(gmail_user, to, msg.as_string()) 
   # Should be mailServer.quit(), but that crashes... 
   mailServer.close()


def addbook(request,docid,username):
	patientname = request.GET.get('patient-name','')
	idcard = request.GET.get('id-card','')
	booktime = request.GET.get('booktime','')
	phone = request.GET.get('phone','')
	doc = doctor.objects.get(doctorid = docid)
	docprof = doc.prof
	user = users.objects.get(username = username)
	hos = doc.hos
	hos.patientnum = str(int(hos.patientnum)+1)
	hos.save()
	dep = doc.dep
	user.books_set.create(doc = doc, hospital = hos.name,depart = dep.departName,docprof= doc.prof,hosAddr = hos.address, time = booktime, patientName =patientname, patientID = idcard,tel = phone, bookID = idcard)
	mail(doc.docmail, 
   "Hello from python!", 
   "This is a email sent with python", 
   "1.jpg")
	return render_to_response('book_succeed.html',{'user':user})

def mybook(request,username):
	user = users.objects.get(username = username)
	bookList = user.books_set.all()
	return render_to_response('mybook.html',{'bookList':bookList,'user':user})            

def visitForm(request,docid,username):
	user = users.objects.get(username = username)
	doc = doctor.objects.get(doctorid = docid)
	hos = doc.hos
	return render_to_response('visitForm.html',{'doc':doc,'hos':hos,'user':user})