# Generated by Django 4.1.13 on 2024-06-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_rename_it_fiels_it_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='related',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=100)),
            ],
        ),
    ]
