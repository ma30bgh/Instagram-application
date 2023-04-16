# Generated by Django 4.2 on 2023-04-16 20:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='phone number is not correct', regex='\\A(09)(0|1|2|3)[0-9]{7}\\d\\z')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]