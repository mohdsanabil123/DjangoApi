# Generated by Django 4.1.7 on 2023-08-07 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeesId',
            new_name='EmployeeId',
        ),
    ]
