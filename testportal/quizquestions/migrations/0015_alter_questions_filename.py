# Generated by Django 5.0.3 on 2024-03-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizquestions', '0014_alter_questions_branch_alter_questions_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='filename',
            field=models.CharField(max_length=500),
        ),
    ]
