# Generated by Django 2.1.7 on 2019-03-21 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=7, verbose_name='use Male/Female')),
                ('qualification', models.CharField(max_length=20, verbose_name='within 20 letters')),
                ('dateOfBirth', models.DateField()),
                ('shortBio', models.CharField(max_length=85, verbose_name='within 85 letters')),
                ('email', models.EmailField(max_length=30)),
                ('homeDistrict', models.CharField(max_length=20)),
                ('currentLocation', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=400)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
    ]
