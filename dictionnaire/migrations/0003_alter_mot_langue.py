# Generated by Django 5.1.1 on 2024-09-19 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire', '0002_mot_image_illustrative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mot',
            name='langue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mots', to='dictionnaire.langue'),
        ),
    ]
