# Generated by Django 4.1.1 on 2022-09-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_article_alternative_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='articles',
            field=models.ManyToManyField(related_name='group', to='backend.article'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_group',
        ),
        migrations.AddField(
            model_name='article',
            name='article_group',
            field=models.Field(null=True),
        ),
    ]
