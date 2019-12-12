from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=400)

    def __str__(self):
        return " written by ".join([self.title,self.author])

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_loan = models.DateTimeField('Date of Loan')

    def __str__(self):
        message = "\n is on loan to ".join([str(self.book),str(self.person)])
        return "\n from: ".join([message,str(self.date_of_loan)])

    def __eq__(self, other):
        return self.book == other.book and self.person == other.person
