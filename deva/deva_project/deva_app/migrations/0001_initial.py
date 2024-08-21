# Generated by Django 4.2.15 on 2024-08-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_course', models.CharField(max_length=50)),
                ('describe', models.TextField(default='no describe', null=True)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
