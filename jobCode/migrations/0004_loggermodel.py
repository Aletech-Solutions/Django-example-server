# Generated by Django 4.2.5 on 2023-09-26 16:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jobCode', '0003_alter_locationmodel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggerModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('endpoint', models.CharField(max_length=255)),
                ('payload', models.TextField()),
                ('method', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'loggermodel',
            },
        ),
    ]
