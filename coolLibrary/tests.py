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


class IndexViewTest(TestCase):

    def test_index_shows_only_avaible_books(self):
        client = Client()
        book = Book(title='test book', author='test author', quantity=0)
        book.save()

        response = client.get('/coolLibrary/')
        self.assertNotContains(response,'test book : test author')


class DonateBookViewTest(TestCase):

    def test_insert_same_book_twice_increase_book_quantity(self):
        client = Client()
        client.post('/coolLibrary/insertBookInLibrary/', {'title' : 'test book', 'author' : 'test author'} )
        client.post('/coolLibrary/insertBookInLibrary/', {'title' : 'test book', 'author' : 'test author'} )

        book = Book.objects.get(title='test book', author='test author')
        self.assertEqual(book.quantity , 2)


class ManageLoanBookViewTest(TestCase):

    def test_loan_a_book_decrease_his_quantity(self):
        client = Client()
        user = User.objects.create_user(username='testuser', email='test@mail.it', password='test')
        book = Book(title='test book', author='test author')
        book.save()
        user.save()
        book_id = Book.objects.get(title='test book', author='test author').id
        response = client.login(username='testuser', password='test')

        if response:
            client.post(f'/coolLibrary/{book_id}/manageLoans/', {})
            book = Book.objects.get(title='test book', author='test author')
            self.assertEqual(book.quantity, 0)
        else:
            print('Login Fallito')
            self.assertFalse()
            

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


