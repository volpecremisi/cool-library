from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.urls import reverse

from .models import Book, Loan

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'coolLibrary/index.html'
    context_object_name = 'book_lists'

    def get_queryset(self):
        """
        Return the last ten Books insered or updated in the library
        """
        topTenBooks = Book.objects.all()
        topTenBooks = list(topTenBooks)
        topTenBooks.reverse()
        return topTenBooks[:10]


class SelectionView(generic.DetailView):
    model = Book
    template_name = 'coolLibrary/selection.html'

class AuthenticationView(generic.TemplateView):
    template_name = 'coolLibrary/authentication.html'

class RegisterView(generic.TemplateView):
    template_name = 'coolLibrary/register.html'

def checkLogin(request, book_id):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('coolLibrary:selection', args=(book_id,)))
    return HttpResponseRedirect(reverse('coolLibrary:authentication'))

def loginUser(request):
    user_username = request.POST['username']
    user_psw = request.POST['psw']
    user_auth = authenticate(request, username=user_username, password=user_psw)
    print(user_auth)
    if user_auth is None:
        return HttpResponseRedirect(reverse('coolLibrary:register'))
    login(request=request, user=user_auth)
    return HttpResponseRedirect(reverse('coolLibrary:index'))

def manageLoans(request, book_id):
    book_to_loan = get_object_or_404(Book, pk= book_id)
    user = request.user
    date = timezone.now()
    newLoans = Loan(book = book_to_loan, person = user, date_of_loan = date)
    newLoans.save()
    return HttpResponseRedirect(reverse('coolLibrary:index'))

def addNewUser(request):
    user_username = request.POST['username']
    user_first_name = request.POST['first_name']
    user_last_name = request.POST['last_name']
    user_password = request.POST['psw']
    user_mail = request.POST['mail']
    user = User.objects.create_user(username=user_username, email=user_mail, password=user_password)
    user.last_name = user_last_name
    user.first_name = user_first_name
    user.save()
    return HttpResponseRedirect(reverse('coolLibrary:authentication'))
