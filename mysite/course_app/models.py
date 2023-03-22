from django.db import models


class courseApplication(models.Model):
    COURSE1 = "Monday 6-6:50"
    COURSE2= "Tuesday 6-6:50"
    COURSE3= "Wednesday 2-2:50"
    Course_Choices = [(COURSE1,"Monday 6-6:50"), (COURSE2, "Tuesday 6-6:50"), (COURSE3, "Wednesday 2-2:50")]
    Discussion_Time_1 = models.CharField(max_length=100, choices = Course_Choices)
    Discussion_Time_2 = models.CharField(max_length=100, choices = Course_Choices)
    First_and_Last_Name = models.CharField(max_length=100, blank=True)
    Resume = models.FileField(upload_to='resumes/')
    Cover_Letter = models.FileField(upload_to='cover_letters/')
    Reference_Letter = models.FileField(upload_to='reference_letters/')
