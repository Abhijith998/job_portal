# Generated by Django 4.1.13 on 2024-06-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='save_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checker_data', models.CharField(max_length=100)),
                ('maker_data', models.CharField(max_length=100)),
            ],
        ),
    ]
