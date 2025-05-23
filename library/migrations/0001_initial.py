# Generated by Django 5.2 on 2025-04-15 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('author_name', models.CharField(blank=True, max_length=40, null=True)),
                ('author', models.CharField(blank=True, max_length=40, null=True)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rental_price_day', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rental_period', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold'), ('Rental', 'Rental')], default='Available')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.category')),
            ],
        ),
    ]
