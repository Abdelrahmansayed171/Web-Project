# Generated by Django 4.0.4 on 2022-05-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_student_department_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=240),
        ),
    ]
