# Generated by Django 3.2.4 on 2021-06-18 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210618_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='work_under',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.employees'),
        ),
    ]
