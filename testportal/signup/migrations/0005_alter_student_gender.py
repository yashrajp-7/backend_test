# Generated by Django 5.0.4 on 2024-04-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_student_tabswitchcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=100),
        ),
    ]