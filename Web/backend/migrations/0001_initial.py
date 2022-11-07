# Generated by Django 4.1.1 on 2022-11-07 15:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('lio_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=30)),
                ('Z41', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('refill_unit', models.IntegerField(choices=[(1, 'Millilitres'), (2, 'Centilitres'), (3, 'Decilitres'), (4, 'Litres'), (5, 'Millimetres'), (6, 'Centimetres'), (7, 'Metres'), (8, 'Pieces'), (9, 'Crates'), (10, 'Bottles')], default=1)),
                ('takeout_unit', models.IntegerField(choices=[(1, 'Millilitres'), (2, 'Centilitres'), (3, 'Decilitres'), (4, 'Litres'), (5, 'Millimetres'), (6, 'Centimetres'), (7, 'Metres'), (8, 'Pieces'), (9, 'Crates'), (10, 'Bottles')], default=1)),
                ('alternative_articles', models.ManyToManyField(blank=True, to='backend.article')),
            ],
        ),
        migrations.CreateModel(
            name='Compartment',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('order_point', models.PositiveSmallIntegerField(default=0)),
                ('standard_order_amount', models.PositiveSmallIntegerField(default=0)),
                ('maximal_capacity', models.PositiveSmallIntegerField(default=0)),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('placement', models.CharField(max_length=30, null=True)),
                ('article', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('building', models.CharField(max_length=30)),
                ('floor', models.CharField(max_length=30)),
                ('cost_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.costcenter')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('supplier_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.costcenter')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('user', models.OneToOneField(default='test', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('time_of_transaction', models.DateField(blank=True, default=datetime.datetime(2022, 11, 7, 15, 11, 2, 626299, tzinfo=datetime.timezone.utc), null=True)),
                ('operation', models.IntegerField(choices=[(1, 'Takeout'), (2, 'Return'), (3, 'Replenish'), (4, 'Adjust')], default=1)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.storage')),
            ],
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('compartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.compartment')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField(default=None)),
                ('expected_wait', models.PositiveSmallIntegerField(default=0)),
                ('order_time', models.DateTimeField(default=datetime.datetime.now)),
                ('order_state', models.IntegerField(choices=[], default=1)),
                ('of_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
                ('to_storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.storage')),
            ],
        ),
        migrations.CreateModel(
            name='InputOutput',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('input_unit_name', models.CharField(max_length=30)),
                ('output_unit_name', models.CharField(max_length=30)),
                ('output_unit_per_input_unit', models.PositiveIntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
        migrations.AddField(
            model_name='compartment',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.storage'),
        ),
        migrations.CreateModel(
            name='CentralStorageSpace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleHasSupplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_article_nr', models.CharField(max_length=15, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
                ('article_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_group',
            field=models.ManyToManyField(to='backend.groupinfo'),
        ),
        migrations.CreateModel(
            name='AlternativeArticleName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
    ]
