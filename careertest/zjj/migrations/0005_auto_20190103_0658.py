# Generated by Django 2.1.4 on 2019-01-03 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zjj', '0004_auto_20190103_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobneed',
            name='create_user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qsj.UserHR'),
        ),
        migrations.AlterField(
            model_name='tester',
            name='create_hr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qsj.UserHR'),
        ),
    ]