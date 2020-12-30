from django.db import models


class Contact_data(models.Model):
    name = models.CharField(max_length=250,  unique=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    employee = models.ForeignKey(Contact_data, related_name='phone', default=None, on_delete=models.PROTECT )
    phone = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.phone


class Email(models.Model):
    employee = models.ForeignKey(Contact_data, related_name='email', default=None, on_delete=models.PROTECT )
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.email

