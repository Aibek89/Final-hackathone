# Generated by Django 4.1 on 2022-08-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activation_code',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
