# Generated by Django 5.0.3 on 2024-03-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizquestions', '0009_rename_department_questions_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='branch',
            field=models.CharField(choices=[('Applied Mechanics(Fluid Mechanics)', 'Applied Mechanics(Fluid Mechanics)'), ('Artificial Intilligence & Machinie Learning', 'Artificial Intilligence & Machinie Learning'), ('Computer Science Engineering', 'Computer Science Engineering'), ('Design Engineering', 'Design Engineering'), ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering'), ('Manufacturing Engineering and Industrial Management', 'Manufacturing Engineering and Industrial Management'), ('Manufacturing Solutions', 'Manufacturing Solutions'), ('Mechanical and Aerospace Engineering', 'Mechanical and Aerospace Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Computer engineering', 'Computer engineering'), ('Mechanis & Design', 'Mechanis & Design'), ('Power Electronics & Power Systems', 'Power Electronics & Power Systems'), ('Thermal Engineering', 'Thermal Engineering'), ('Mechanical', 'Mechanical'), ('Industrial', 'Industrial'), ('Production', 'Production'), ('Instrumentation', 'Instrumentation'), ('Chemical', 'Chemical'), ('Computer Science', 'Computer Science'), ('Information Technology', 'Information Technology'), ('Electronics & Telecommunication', 'Electronics & Telecommunication'), ('Product Design', 'Product Design'), ('UI/UX Design', 'UI/UX Design'), ('Automobile', 'Automobile'), ('Interdisciplinary', 'Interdisciplinary')], default='Computer Science Engineering', max_length=100),
        ),
    ]
