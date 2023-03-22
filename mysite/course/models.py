from django.db import models

# Create your models here.

class AddCourseModel(models.Model):
    Course_Name = models.CharField(max_length=100, blank=True)
    Course_ID = models.CharField(max_length=100, blank=True)
    Section = models.CharField(max_length=10, blank=True)
    Marking_Meetings = models.CharField(max_length=10, blank=True)
    Lecture_Times= models.CharField(max_length=100, blank=True)
    Discussion_Times = models.CharField(max_length=100, blank=True)
    Course_Description = models.TextField(blank=True)
    Office_Hours_per_week = models.PositiveIntegerField(blank=True, null=True)



    # def __str__(self):
    #     return self.name