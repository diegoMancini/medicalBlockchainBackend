# Generated by Django 3.0.5 on 2020-04-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('specialty', models.CharField(max_length=20)),
                ('dni', models.IntegerField()),
                ('nro_matricula_nacional', models.IntegerField()),
                ('nro_matricula_provincial', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]