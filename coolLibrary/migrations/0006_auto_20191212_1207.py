# Generated by Django 3.0 on 2019-12-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coolLibrary', '0005_auto_20191212_1158'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set(),
        ),
    ]
