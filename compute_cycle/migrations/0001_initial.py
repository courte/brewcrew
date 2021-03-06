# Generated by Django 2.0 on 2017-12-08 16:17

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
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_date', models.DateTimeField(verbose_name='proposed date')),
                ('fulfilled_date', models.DateTimeField(verbose_name='date meeting occurred')),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compute_cycle.Location')),
            ],
        ),
    ]
