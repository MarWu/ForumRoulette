# Generated by Django 2.1.2 on 2018-10-20 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
