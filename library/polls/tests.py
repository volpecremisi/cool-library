from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.

from .models import Book, Loan

class LoanModelTest(TestCase):

    def test_loanSameBookTwiceBySamePersonIsNotAdmitted(self):
        #Before
        book = Book(title='test book', author='test author')
        user = User(username='testuser', email='test@mail.it', password='test')
        date = timezone.now()
        book.save()
        user.save()

        #Test
        newLoans = Loan(book = book, person = user, date_of_loan = date)
        newLoans.save()
        date = timezone.now()
        loansFirstInsertion = list(Loan.objects.all())
        newLoans = Loan(book = book, person = user, date_of_loan = date)
        newLoans.save()
        loansSecondInsertion = list(Loan.objects.all())

        self.assertEqual(loansFirstInsertion, loansSecondInsertion)

        #After
        Loan.objects.filter(book= book, person= user, date_of_loan= date).delete()
        u = User.objects.get(username = 'testuser')
        u.delete()
        Books.objects.filter(title='test book', author='test author').delete()



