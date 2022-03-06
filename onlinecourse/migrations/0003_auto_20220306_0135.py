# Generated by Django 3.1.3 on 2022-03-06 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220305_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.AddField(
            model_name='question',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
            preserve_default=False,
        ),
    ]
