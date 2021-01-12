# Generated by Django 3.1.5 on 2021-01-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=150, null=True)),
                ('lastName', models.CharField(blank=True, max_length=150, null=True)),
                ('studentId', models.IntegerField(blank=True, null=True)),
                ('level', models.CharField(blank=True, max_length=30, null=True)),
                ('department', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=20, null=True)),
                ('image', models.ImageField(default='studentImages/user.png', upload_to='studentImages')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ver', models.BooleanField(default=False)),
            ],
        ),
    ]