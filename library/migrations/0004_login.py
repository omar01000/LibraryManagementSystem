# Generated by Django 5.2 on 2025-04-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_price_alter_book_rental_price_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
