# Generated by Django 4.0.2 on 2022-03-01 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='age_choices',
            new_name='age_limit',
        ),
    ]