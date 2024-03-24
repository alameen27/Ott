# Generated by Django 5.0.1 on 2024-01-09 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0011_customerprofileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moviekid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to='media/')),
                ('kid_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='ottapp.kidprofile')),
            ],
        ),
    ]