# Generated by Django 2.1.4 on 2018-12-22 00:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('is_crypto', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('source_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_currency', to='currency.Currency')),
                ('target_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_currency', to='currency.Currency')),
            ],
        ),
    ]
