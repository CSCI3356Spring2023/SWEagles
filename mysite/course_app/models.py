from django.db import models


class courseApplicationAllRequired(models.Model):
    COURSE1 = "Monday 6-6:50"
    COURSE2= "Tuesday 6-6:50"
    COURSE3= "Wednesday 2-2:50"
    Course_Name = models.CharField(max_length=100, editable=False)
    Course_Section = models.CharField(max_length=100, editable=False)
    Course_Choices = [(COURSE1,"Monday 6-6:50"), (COURSE2, "Tuesday 6-6:50"), (COURSE3, "Wednesday 2-2:50")]
    Discussion_Time_1 = models.CharField(max_length=100, choices = Course_Choices)
    Discussion_Time_2 = models.CharField(max_length=100, choices = Course_Choices)
    First_and_Last_Name = models.CharField(max_length=100, blank=False)
    Resume = models.FileField(upload_to='course_app/resumes/', blank=False)
    Cover_Letter = models.FileField(upload_to='course_app/cover_letters/', blank = False)
    Reference_Letter = models.FileField(upload_to='course_app/reference_letters/', blank = False)


class courseApplicationOnlyResume(models.Model):
    COURSE1 = "Monday 6-6:50"
    COURSE2= "Tuesday 6-6:50"
    COURSE3= "Wednesday 2-2:50"
    Course_Name = models.CharField(max_length=100, editable=False)
    Course_Section = models.CharField(max_length=100, editable=False)
    Course_Choices = [(COURSE1,"Monday 6-6:50"), (COURSE2, "Tuesday 6-6:50"), (COURSE3, "Wednesday 2-2:50")]
    Discussion_Time_1 = models.CharField(max_length=100, choices = Course_Choices)
    Discussion_Time_2 = models.CharField(max_length=100, choices = Course_Choices)
    First_and_Last_Name = models.CharField(max_length=100, blank=False)
    Resume = models.FileField(upload_to='course_app/resumes/', blank=False)
    Cover_Letter = models.FileField(upload_to='course_app/cover_letters/', blank = True)
    Reference_Letter = models.FileField(upload_to='course_app/reference_letters/', blank = True)
