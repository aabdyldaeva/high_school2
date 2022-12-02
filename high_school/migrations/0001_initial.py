# Generated by Django 3.2 on 2022-12-02 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=290, verbose_name='Teacher name')),
                ('class_name', models.CharField(choices=[('a_class', 'A_class'), ('b_class', 'B_class'), ('c_class', 'C_class')], max_length=50, verbose_name='Class name')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Pupil name')),
                ('birth_date', models.DateField(max_length=20, verbose_name='Date of Birth of Pupil')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='high_school.teacher')),
            ],
        ),
    ]
