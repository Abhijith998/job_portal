# Generated by Django 4.1.13 on 2024-06-15 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='related',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.it_fields'),
        ),
    ]
