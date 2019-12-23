from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=400)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = (("title","author"),)

    def __str__(self):
        return f"{self.title} written by {self.author}"


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("book","person"),)

    def __str__(self):
        message = "\n is on loan to ".join([str(self.book),str(self.person)])
        return message

    def __eq__(self, other):
        return self.book == other.book and self.person == other.person


class Date(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    date_of_loan = models.DateTimeField('Date of Loan')
    loan_date_expire = models.DateTimeField('Loan End Date')

    def __str__(self):
        return f"The loan '{self.loan}' is from {self.date_of_loan} to {self.loan_date_expire}"
