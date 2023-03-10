# Generated by Django 4.1.5 on 2023-01-28 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empapp', '0002_remove_employee_dept_remove_employee_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('hiredate', models.DateField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.role')),
            ],
        ),
    ]
