from django.shortcuts import render
from books.models import books
from users.models import users
from django.shortcuts import render_to_response
# Create your views here.
	
def deletebook(request, bookid, username):
	user = users.objects.get(username = username)
	books.objects.filter(bookID = bookid).delete()
	bookList = user.books_set.all()
	return render_to_response('mybook.html',{'bookList':bookList,'user':user})  
	