from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=400)

    def __str__(self):
        return " : ".join([self.title,self.author])


'''
# Qui ci vorrebbe una tebella?
class Loans(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_of_loan = models.DateTimeField('Date of Loan')

class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mail = models.CharField(max_length=200)

    def __str__(self):
        return " ,".join([self.name,self.surname,self.mail])
'''