# Generated by Django 3.0 on 2019-12-11 15:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_loans'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loans',
            new_name='Loan',
        ),
    ]
