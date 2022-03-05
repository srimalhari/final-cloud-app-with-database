# Generated by Django 3.1.3 on 2022-03-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='lesson_id',
            new_name='lesson',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
