# Generated by Django 3.1.4 on 2020-12-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_remove_email_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
