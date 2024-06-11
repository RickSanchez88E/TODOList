from django.db import models


class Person(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    dob = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ['name']
