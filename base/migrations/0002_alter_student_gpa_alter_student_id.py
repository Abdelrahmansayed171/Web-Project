# Generated by Django 4.0.4 on 2022-05-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='GPA',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]