# Generated by Django 5.1.4 on 2024-12-23 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_enrollment_faculty_subject_subjectrating_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(name="category", table="category",),
        migrations.AlterModelTable(name="course", table="course",),
    ]
