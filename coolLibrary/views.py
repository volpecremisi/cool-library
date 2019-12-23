from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.db.utils import IntegrityError

from .models import Book, Loan, Date

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'coolLibrary/index.html'
    context_object_name = 'book_lists'

    def get_queryset(self):
        """
        Return the last ten Books insered or updated in the library with quantity > 0
        """
        topTenBooks = Book.objects.all().exclude(quantity=0)
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

class DonateBookView(generic.TemplateView):
    template_name = 'coolLibrary/donateBook.html'

class ShowUserLoanedBooksView(generic.ListView):
    template_name = 'coolLibrary/showLoans.html'
    context_object_name = 'book_lists'

    def get_queryset(self):
        """
        Return the books loaned by a logged user
        """
        user = self.request.user
        print(user)
        books_query_set = Loan.objects.filter(person=user).values_list('book', flat=True)
        books_query_set = Book.objects.filter(pk__in=books_query_set)
        return books_query_set

def insertBookInLibrary(request):
    book_title = request.POST['title']
    book_author = request.POST['author']
    try:
        book_in_library = Book.objects.get(title=book_title, author=book_author)
        book_in_library.quantity += 1
        book_in_library.save()
    except (KeyError, Book.DoesNotExist) as dne:
        book_to_insert = Book(title=book_title,author=book_author)
        book_to_insert.save()
    finally:
        return HttpResponseRedirect(reverse('coolLibrary:index'))

def checkLogin(request, book_id):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('coolLibrary:selection', args=(book_id,)))
    return HttpResponseRedirect(reverse('coolLibrary:authentication'))

def loginUser(request):
    user_username = request.POST['username']
    user_psw = request.POST['psw']
    user_auth = authenticate(request, username=user_username, password=user_psw)
    if user_auth is None:
        return render(request, 'coolLibrary/authentication.html', {
            'error_message': "Username or Password incorrect. Please retry.",
        })
    login(request=request, user=user_auth)
    return HttpResponseRedirect(reverse('coolLibrary:index'))

def manageLoans(request, book_id):
    book_to_loan = get_object_or_404(Book, pk= book_id)
    book_to_loan.quantity = book_to_loan.quantity-1
    book_to_loan.save()
    user = request.user
    date_loan_begin = timezone.now()
    date_loan_end = date_loan_begin + timedelta(days=30)
    newLoans = Loan(book = book_to_loan, person = user)
    newLoans.save()
    dates = Date(loan=newLoans, date_of_loan=date_loan_begin, loan_date_expire=date_loan_end)
    dates.save()
    return HttpResponseRedirect(reverse('coolLibrary:index'))

def addNewUser(request):
    user_username = request.POST['username']
    user_first_name = request.POST['first_name']
    user_last_name = request.POST['last_name']
    user_password = request.POST['psw']
    user_mail = request.POST['mail']
    try:
        user = User.objects.create_user(username=user_username, email=user_mail, password=user_password)
        user.last_name = user_last_name
        user.first_name = user_first_name
        user.save()
        return HttpResponseRedirect(reverse('coolLibrary:authentication'))
    except IntegrityError as ie:
        return render(request, 'coolLibrary/register.html', {
            'error_message': "This username is already catched! Try something else please.",
        })


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('coolLibrary:index'))