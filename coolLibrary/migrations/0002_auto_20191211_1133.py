# Generated by Django 3.0 on 2019-12-11 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coolLibrary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loans',
            name='book',
        ),
        migrations.RemoveField(
            model_name='loans',
            name='person',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.DeleteModel(
            name='Loans',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
