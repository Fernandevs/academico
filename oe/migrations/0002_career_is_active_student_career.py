# Generated by Django 4.0.3 on 2022-03-30 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='career',
            field=models.ManyToManyField(to='oe.career'),
        ),
    ]
