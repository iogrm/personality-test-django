# Generated by Django 3.2.11 on 2022-06-25 04:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import persona.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('cover', models.FileField(upload_to='files/category_cover/', validators=[persona.models.validate_file_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Mbti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbti', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('cover', models.FileField(upload_to='files/mbti_avatar/')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('loc', models.CharField(max_length=128)),
                ('mbti', models.CharField(max_length=128)),
                ('description', ckeditor.fields.RichTextField()),
                ('picture', models.FileField(upload_to='files/place_cover/', validators=[persona.models.validate_file_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('symbol', models.CharField(max_length=128)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=512)),
                ('first_name', models.CharField(max_length=128, null=True)),
                ('sir_name', models.CharField(max_length=128, null=True)),
                ('mbti', models.CharField(max_length=8)),
                ('birth', models.DateField(null=True)),
                ('isFemale', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', ckeditor.fields.RichTextField()),
                ('trait_agree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trait_agree', to='persona.trait')),
                ('trait_disagree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trait_disagree', to='persona.trait')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('isFemale', models.BooleanField()),
                ('cover', models.FileField(upload_to='files/character_cover/', validators=[persona.models.validate_file_extension])),
                ('description', ckeditor.fields.RichTextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.category')),
                ('mbti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.mbti')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField()),
                ('answer', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.userprofile')),
            ],
        ),
    ]