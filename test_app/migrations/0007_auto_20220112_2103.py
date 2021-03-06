# Generated by Django 2.2.10 on 2022-01-12 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_auto_20220112_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='polls',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='test_app.Polls'),
        ),
        migrations.DeleteModel(
            name='UserAnswers',
        ),
    ]
