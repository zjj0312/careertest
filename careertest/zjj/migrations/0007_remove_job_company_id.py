# Generated by Django 2.1.4 on 2019-01-03 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zjj', '0006_auto_20190103_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_id',
        ),
    ]