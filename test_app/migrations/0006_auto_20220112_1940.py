# Generated by Django 2.2.10 on 2022-01-12 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_auto_20220111_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Polls')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Questions')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('polls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Polls')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='test_app.Answers')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Users'),
        ),
    ]
