# Generated by Django 4.1.1 on 2022-09-24 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='pants',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='shirt',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='shoes',
        ),
        migrations.DeleteModel(
            name='ClothPart',
        ),
        migrations.AddField(
            model_name='cloth',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='employees.employee'),
        ),
    ]
