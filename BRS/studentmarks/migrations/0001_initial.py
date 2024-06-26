# Generated by Django 5.0.4 on 2024-05-03 16:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplines',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_student', models.UUIDField()),
                ('id_discipline', models.UUIDField()),
                ('value', models.FloatField()),
                ('mark_type_id', models.UUIDField()),
                ('term_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='MarkType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SliceType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=40)),
                ('start_data', models.DateField()),
                ('end_data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type_id', models.UUIDField()),
                ('start_data', models.DateField()),
                ('end_data', models.DateField()),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeTerm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
