# Generated by Django 4.1.3 on 2023-08-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LisheApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='settings_name', max_length=256)),
                ('value', models.CharField(blank=True, default='', max_length=256)),
            ],
        ),
    ]