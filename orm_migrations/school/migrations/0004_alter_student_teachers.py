# Generated by Django 4.2.6 on 2023-11-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(to='school.teacher'),
        ),
    ]
