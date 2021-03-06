# Generated by Django 3.1.2 on 2020-10-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.IntegerField(default=0)),
                ('course', models.CharField(max_length=100)),
                ('fee', models.FloatField(default=0.0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
