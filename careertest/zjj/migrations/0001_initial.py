# Generated by Django 2.1.4 on 2018-12-29 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qsj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=100)),
                ('isdelete', models.BooleanField(default=False)),
                ('company_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='qsj.Company')),
                ('moding_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qsj.Moding')),
            ],
        ),
        migrations.CreateModel(
            name='Jobneed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobdescription', models.CharField(max_length=1024)),
                ('jobrequirements', models.CharField(max_length=1024)),
                ('isdelete', models.BooleanField(default=False)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zjj.Job')),
                ('moding_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qsj.Moding')),
            ],
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=1024)),
                ('status', models.CharField(max_length=280)),
                ('isdelete', models.BooleanField(default=False)),
                ('jobneed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zjj.Jobneed')),
            ],
        ),
    ]
