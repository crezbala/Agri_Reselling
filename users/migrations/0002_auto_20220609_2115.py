# Generated by Django 3.1.7 on 2022-06-09 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Voted_spaces',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='brandname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='usertype',
        ),
    ]
