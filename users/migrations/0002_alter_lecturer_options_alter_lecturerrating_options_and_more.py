# Generated by Django 5.1.4 on 2024-12-23 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="lecturer", options={"managed": True},),
        migrations.AlterModelOptions(name="lecturerrating", options={"managed": True},),
        migrations.AlterModelOptions(name="student", options={"managed": True},),
    ]