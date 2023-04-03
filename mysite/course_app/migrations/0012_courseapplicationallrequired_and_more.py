# Generated by Django 4.1.5 on 2023-04-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0011_alter_courseapplication_cover_letter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseApplicationAllRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(editable=False, max_length=100)),
                ('Course_Section', models.CharField(editable=False, max_length=100)),
                ('Discussion_Time_1', models.CharField(choices=[('Monday 6-6:50', 'Monday 6-6:50'), ('Tuesday 6-6:50', 'Tuesday 6-6:50'), ('Wednesday 2-2:50', 'Wednesday 2-2:50')], max_length=100)),
                ('Discussion_Time_2', models.CharField(choices=[('Monday 6-6:50', 'Monday 6-6:50'), ('Tuesday 6-6:50', 'Tuesday 6-6:50'), ('Wednesday 2-2:50', 'Wednesday 2-2:50')], max_length=100)),
                ('First_and_Last_Name', models.CharField(max_length=100)),
                ('Resume', models.FileField(upload_to='course_app/resumes/')),
                ('Cover_Letter', models.FileField(upload_to='course_app/cover_letters/')),
                ('Reference_Letter', models.FileField(upload_to='course_app/reference_letters/')),
            ],
        ),
        migrations.RenameModel(
            old_name='courseApplication',
            new_name='courseApplicationOnlyResume',
        ),
    ]
