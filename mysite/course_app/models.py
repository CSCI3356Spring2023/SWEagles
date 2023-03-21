from django.db import models
from django import forms


class courseApplication(models.Model):
    First_and_Last_Name = models.CharField(max_length=100, blank=True)
    pdf_file = forms.FileField()
    COURSE1 = "Monday 6-6:50, CSCI 1101.01.01"
    COURSE2= "Tuesday 6-6:50, CSCI 1101.01.02"
    COURSE3= "Wednesday 2-2:50, CSCI 1101.01.03"
    Course_Choices = [(COURSE1,"Discussion Times: Monday 6-6:50"), (COURSE2, "Discussion Times: Tuesday 6-6:50"), (COURSE3, "Discussion Times: Wednesday 2-2:50")]
    courses = models.CharField(max_length=100, choices = Course_Choices)

# Create your models here.
