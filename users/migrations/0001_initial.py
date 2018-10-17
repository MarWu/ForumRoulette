# Generated by Django 2.1.2 on 2018-10-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('post_count', models.IntegerField(default=0)),
            ],
        ),
    ]