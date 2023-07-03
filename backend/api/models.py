from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    class EmploymentType(models.TextChoices):
        EMPLOYEE = "EMP", _('Employee')
        MEMBER = "MEM", _('Member')

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    employment_type = models.CharField(
        max_length=3,
        choices=EmploymentType.choices,
        default=EmploymentType.MEMBER,
    )
    speciality = models.CharField(max_length=50, blank=True, null=True)

    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.employment_type}'

    def __repr__(self):
        return f'ID: {self.id} | {self.first_name} {self.last_name}'


class Project(models.Model):
    class ProjectType(models.TextChoices):
        INTERNAL = 'INT', _('Internal')
        EXTERNAL = 'EXT', _('External')

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    short_description = models.CharField(max_length=50, null=True, blank=True)
    project_type = models.CharField(
        max_length=3,
        choices=ProjectType.choices,
        default=ProjectType.INTERNAL,
    )

    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    contributors = models.ManyToManyField(Person, related_name='projects')

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'ID: {self.id} | {self.title}'

