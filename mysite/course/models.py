from django.db import models

# Create your models here.
COLORS= (
    ('R', 'Red'),
    ('B', 'Yellow'),
    ('G', 'White'),
)
class AddCourse(models.Model):
    Course_Name = models.CharField(max_length=100)
    Course_ID = models.CharField(max_length=100)
    Section = models.CharField(max_length=10)
    Marking_Meetings = models.CharField(max_length=10)
    Lecture_Times= models.DateTimeField()
    Discussion_Times = models.DateTimeField()
    Course_Description = models.TextField()
    Instructor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Office_Hours_per_week = models.PositiveIntegerField()


    # def __str__(self):
    #     return self.name