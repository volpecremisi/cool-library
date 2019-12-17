from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.utils import IntegrityError

from .models import Book, Loan


class BookModelTest(TestCase):

    def test_insert_same_book_twice_raise_integrity_error(self):
        book = Book(title='test book', author='test author')
        book.save()

        same_book = Book(title='test book', author='test author')
        with self.assertRaises(IntegrityError):
            same_book.save()


class DonateBookViewTest(TestCase):

    def test_insert_same_book_twice_increase_book_quantity(self):
        client = Client()
        client.post('/coolLibrary/insertBookInLibrary/', {'title' : 'test book', 'author' : 'test author'} )
        client.post('/coolLibrary/insertBookInLibrary/', {'title' : 'test book', 'author' : 'test author'} )

        book = Book.objects.get(title='test book', author='test author')
        self.assertEqual(book.quantity , 2)


class LoanModelTest(TestCase):

    def test_loan_same_book_to_same_person_generate_integrity_error(self):
        book = Book(title='test book', author='test author')
        user = User(username='testuser', email='test@mail.it', password='test')
        date = timezone.now()
        book.save()
        user.save()
        newLoans = Loan(book = book, person = user, date_of_loan = date)
        newLoans.save()

        with self.assertRaises(IntegrityError):
            date = timezone.now()
            newLoans = Loan(book = book, person = user, date_of_loan = date)
            newLoans.save()


class UserRegistrationTest(TestCase):

    def test_register_with_already_used_account_generate_error_message(self):
        client = Client()
        username = 'nametest'
        mail = 'mailtest'
        psw = 'pswtest'
        first_name = 'fntest'
        last_name = 'lntest'
        client.post('/coolLibrary/addNewUser/', {
                                                'username' : username,
                                                'mail' : mail ,
                                                'first_name' : first_name,
                                                'last_name' : last_name,
                                                'psw' : psw,
                                                })

        response = client.post('/coolLibrary/addNewUser/', {
                                                            'username' : username,
                                                            'mail' : mail ,
                                                            'first_name' : first_name,
                                                            'last_name' : last_name,
                                                            'psw' : psw,
                                                          })
        self.assertContains(response,'This username is already catched! Try something else please.')


'''
class LoginTest(TestCase):

    def test_wrong_login_credential_generate_error_message(self):
'''