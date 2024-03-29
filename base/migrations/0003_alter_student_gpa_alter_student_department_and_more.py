# Generated by Django 4.0.4 on 2022-05-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_student_gpa_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='GPA',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('computer science', 'COMPUTER SCIENCE'), ('information system', 'INFORMATION SYSTEM'), ('information technology', 'INFORMATION TECHNOLOGY'), ('artificial intelligence', 'ARTIFICIAL INTELLIGENCE'), ('decision support system', 'DECISION SUPPORT SYSTEM'), ('general', 'GENERAL')], default='general', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=32),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_Num',
            field=models.CharField(blank=True, max_length=124, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], default='inactive', max_length=32),
        ),
    ]
