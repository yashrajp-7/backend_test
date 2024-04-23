# Generated by Django 5.0.4 on 2024-04-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizquestions', '0015_alter_questions_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrevQuestionPaperSet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=100)),
                ('filename', models.FileField(upload_to='prevfiles')),
                ('stream', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('M.S', 'M.S'), ('B.Des', 'B.Des'), ('M.Des', 'M.Des')], max_length=100)),
                ('branch', models.CharField(choices=[('Applied Mechanics(Fluid Mechanics)', 'Applied Mechanics(Fluid Mechanics)'), ('Artificial Intilligence & Machinie Learning', 'Artificial Intilligence & Machinie Learning'), ('Computer Science Engineering', 'Computer Science Engineering'), ('Design Engineering', 'Design Engineering'), ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering'), ('Manufacturing Engineering and Industrial Management', 'Manufacturing Engineering and Industrial Management'), ('Manufacturing Solutions', 'Manufacturing Solutions'), ('Mechanical and Aerospace Engineering', 'Mechanical and Aerospace Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Computer engineering', 'Computer engineering'), ('Mechanis & Design', 'Mechanis & Design'), ('Power Electronics & Power Systems', 'Power Electronics & Power Systems'), ('Thermal Engineering', 'Thermal Engineering'), ('Mechanical', 'Mechanical'), ('Industrial', 'Industrial'), ('Production', 'Production'), ('Instrumentation', 'Instrumentation'), ('Chemical', 'Chemical'), ('Computer Science', 'Computer Science'), ('Information Technology', 'Information Technology'), ('Electronics & Telecommunication', 'Electronics & Telecommunication'), ('Product Design', 'Product Design'), ('UI/UX Design', 'UI/UX Design'), ('Automobile', 'Automobile'), ('Interdisciplinary', 'Interdisciplinary')], max_length=100)),
            ],
        ),
    ]
