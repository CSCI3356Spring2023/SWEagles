# Generated by Django 4.1.7 on 2023-04-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0005_studentuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="hire_status",
            field=models.CharField(default="unhired", max_length=7),
        ),
    ]
