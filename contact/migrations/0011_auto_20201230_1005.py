# Generated by Django 3.1.4 on 2020-12-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_remove_email_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_data',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]