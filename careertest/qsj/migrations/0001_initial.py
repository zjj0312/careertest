# Generated by Django 2.1.4 on 2018-12-29 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Moding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to='')),
                ('factor1_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor2_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor3_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor4_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor5_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor6_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor7_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor8_ex_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('factor1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qsj.Factor')),
            ],
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserExpert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserHR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qsj.Company')),
            ],
        ),
    ]
