# Generated by Django 3.2.11 on 2022-06-25 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_place_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='mbti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.mbti'),
        ),
    ]
