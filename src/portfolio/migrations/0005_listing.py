# Generated by Django 5.0.2 on 2024-03-02 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_band_year_formed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.band')),
            ],
        ),
    ]
