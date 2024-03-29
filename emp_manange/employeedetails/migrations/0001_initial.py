# Generated by Django 5.0 on 2024-01-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lastname', models.CharField(max_length=200)),
                ('Qualification', models.CharField(max_length=100)),
                ('Experience', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Phonenumber', models.BigIntegerField()),
                ('State', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Areacode', models.CharField(max_length=50)),
            ],
        ),
    ]
