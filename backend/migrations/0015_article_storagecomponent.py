# Generated by Django 4.1.1 on 2022-09-29 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_merge_20220929_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='storageComponent',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
