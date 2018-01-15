from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CreateAssignment(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    submit_date = models.DateField()
    submit_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubmitAssignment(models.Model):
    GRAD_CHOICES = (('a+', 'A+'), ('a', 'A'), ('b+', 'B+'), ('b', 'B'), ('c', 'C'), ('d', 'D'))

    assignment = models.ForeignKey(CreateAssignment)
    description = models.CharField(max_length=1000)
    file = models.FileField()
    submit_by = models.ForeignKey(User)
    submit_date = models.DateField(null=True)
    grad = models.CharField(choices=GRAD_CHOICES, max_length=50, null=True)

    def __str__(self):
        return self.assignment.title
