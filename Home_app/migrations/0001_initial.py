# Generated by Django 3.1.7 on 2022-06-09 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='prof',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='Check', max_length=200, null=True)),
                ('password', models.CharField(default='Check', max_length=200, null=True)),
                ('userName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
