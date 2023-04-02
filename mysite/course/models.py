from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
DAYS_OF_WEEK = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
class AddCourseModel(models.Model):
    Instructor_ID = models.CharField(max_length=10, blank=True)
    Course_Name = models.CharField(max_length=100, blank=True)
    Course_ID = models.CharField(max_length=100, blank=True)
    Section = models.CharField(max_length=10, blank=True)
    Marking_Meetings = models.BooleanField(max_length=10, blank=True)
    Lecture_Days = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=3, max_length=3, blank= True)
    Lecture_Times= models.TimeField(auto_now=False, auto_now_add=False)
    Discussion_Days = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=3, max_length=3, blank= True)
    Discussion_Times = models.DurationField(max_length=100, blank=True)
    Course_Description = models.TextField(blank=True)
    Office_Hours_per_week = models.PositiveIntegerField(blank=True, null=True)
    TA_Positions = models.PositiveIntegerField(blank=True, null=True)



    # def __str__(self):
    #     return self.name