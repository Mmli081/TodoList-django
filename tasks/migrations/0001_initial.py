# Generated by Django 4.0.6 on 2022-08-09 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('has_done', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('day', 'Day'), ('everyday', 'EveryDay'), ('monday', 'Mondays'), ('tuesday', 'Tuesdays'), ('wednesday', 'Wednesdays'), ('thursday', 'Thursdays'), ('friday', 'Fridays'), ('saturday', 'Saturdays'), ('sunday', 'Sundays')], default='day', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.day')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
