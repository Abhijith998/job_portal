# Generated by Django 4.1.13 on 2024-06-16 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_alter_related_dept'),
        ('user_app', '0003_register_user_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.it_fields')),
            ],
        ),
    ]
