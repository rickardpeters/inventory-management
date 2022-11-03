# Generated by Django 4.1.1 on 2022-11-01 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_articlehassupplier_supplier_article_nr'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternativeArticleName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
    ]
