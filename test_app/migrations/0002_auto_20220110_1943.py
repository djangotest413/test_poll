# Generated by Django 2.2.10 on 2022-01-10 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polls',
            old_name='name',
            new_name='poll_name',
        ),
    ]