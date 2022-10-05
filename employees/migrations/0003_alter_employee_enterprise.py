# Generated by Django 4.1.1 on 2022-09-24 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_profile_enterprise'),
        ('employees', '0002_cloth_remove_employee_pants_remove_employee_shirt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cloths', to='users.enterprise'),
        ),
    ]