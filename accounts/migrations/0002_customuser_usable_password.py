# Generated by Django 5.1.3 on 2024-11-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='usable_password',
            field=models.BooleanField(default=True),
        ),
    ]
