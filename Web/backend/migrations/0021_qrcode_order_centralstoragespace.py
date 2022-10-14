# Generated by Django 4.1.1 on 2022-10-06 12:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_storagespace_storageunit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.CharField(max_length=15,
                 primary_key=True, serialize=False)),
                ('storage_space', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.storagespace')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField(default=None)),
                ('expectedWait', models.PositiveSmallIntegerField(default=0)),
                ('orderTime', models.DateTimeField(default=datetime.datetime.now)),
                ('hasArrived', models.BooleanField(default=False)),
                ('ofArticle', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
                ('toStorageUnit', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='backend.storageunit')),
            ],
        ),
        migrations.CreateModel(
            name='CentralStorageSpace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('article', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
    ]
