# Generated by Django 3.1.4 on 2020-12-29 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_email_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='phone',
        ),
    ]
