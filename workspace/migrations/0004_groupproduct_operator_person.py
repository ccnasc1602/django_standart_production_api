# Generated by Django 3.1.5 on 2021-01-31 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_auto_20210130_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(auto_created=True, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.IntegerField(unique=True, verbose_name='document number')),
                ('nickname', models.CharField(max_length=100, verbose_name='nickname')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=20, verbose_name='gender')),
                ('code_area', models.CharField(max_length=2, null=True, verbose_name='code area')),
                ('mobile_number', models.CharField(max_length=10, verbose_name='mobile_number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('code', models.IntegerField(auto_created=True, unique=True, verbose_name='code')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='workspace.person')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('turn', models.CharField(max_length=10, verbose_name='turn')),
            ],
        ),
    ]
