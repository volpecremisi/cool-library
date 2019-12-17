# Generated by Django 3.0 on 2019-12-11 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coolLibrary', '0002_auto_20191211_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_loan', models.DateTimeField(verbose_name='Date of Loan')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coolLibrary.Book')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
