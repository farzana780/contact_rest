# Generated by Django 3.1.4 on 2020-12-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_email_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]