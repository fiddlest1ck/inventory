# Generated by Django 2.0.1 on 2018-01-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_number', models.PositiveIntegerField(blank=True)),
                ('out_number', models.PositiveIntegerField(blank=True)),
                ('in_date', models.DateTimeField(blank=True)),
                ('symbol_and_doc_number', models.CharField(blank=True, max_length=255)),
                ('item_name', models.CharField(blank=True, max_length=255)),
                ('item_description', models.CharField(blank=True, max_length=255)),
                ('item_state', models.CharField(blank=True, max_length=255)),
                ('item_price', models.FloatField(blank=True)),
                ('number_of_incoming', models.PositiveIntegerField(blank=True)),
                ('number_of_outgoing', models.PositiveIntegerField(blank=True)),
                ('number_result', models.IntegerField(blank=True)),
                ('incoming_value', models.CharField(blank=True, max_length=255)),
                ('outgoing_value', models.CharField(blank=True, max_length=255)),
                ('value_result', models.CharField(blank=True, max_length=255)),
                ('next_number', models.IntegerField(blank=True)),
                ('additionals', models.TextField(blank=True)),
            ],
        ),
    ]
