from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=290, verbose_name='Teacher name')
    class_name = models.CharField(max_length=50, choices=(
        ('a_class', 'A_class'),
        ('b_class', 'B_class'),
        ('c_class', 'C_class')
    ), verbose_name='Class name')

    def __str__(self):
        return self.name


class Pupil(models.Model):
    name = models.CharField(max_length=20, verbose_name='Pupil name')
    birth_date = models.DateField(max_length=20, verbose_name = 'Date of Birth of Pupil')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
