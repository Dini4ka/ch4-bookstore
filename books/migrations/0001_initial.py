# Generated by Django 5.1.3 on 2024-11-17 19:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]