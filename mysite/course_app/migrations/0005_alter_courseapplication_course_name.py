# Generated by Django 4.1.5 on 2023-04-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_courseapplication_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseapplication',
            name='Course_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
