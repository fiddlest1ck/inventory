# Generated by Django 2.0.1 on 2018-01-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_inventory', '0002_record_stock_item_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='item_description',
        ),
        migrations.RemoveField(
            model_name='record',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='record',
            name='item_state',
        ),
        migrations.AddField(
            model_name='record',
            name='item_name_description_state',
            field=models.TextField(blank=True, null=True, verbose_name='Nazwa przedmiotu (obiektu) jego opis i stan'),
        ),
        migrations.AlterField(
            model_name='record',
            name='additionals',
            field=models.TextField(blank=True, null=True, verbose_name='UWAGI (co do miejsca znajdowania sie przedmiotu i inne)'),
        ),
        migrations.AlterField(
            model_name='record',
            name='in_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data przychodu i względnie rozchodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='in_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nr kolejny przychodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='incoming_value',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Wartość przychodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='item_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena jednostkowa'),
        ),
        migrations.AlterField(
            model_name='record',
            name='next_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Przeciwstawny numer kolejny'),
        ),
        migrations.AlterField(
            model_name='record',
            name='number_of_incoming',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ilość przychodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='number_of_outgoing',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ilość rozchodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='number_result',
            field=models.IntegerField(blank=True, null=True, verbose_name='Stan Ilości'),
        ),
        migrations.AlterField(
            model_name='record',
            name='out_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nr kolejny rozchodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='outgoing_value',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Wartość rozchodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='stock_item_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Numer fabryczny przedmiotu (obiektu)'),
        ),
        migrations.AlterField(
            model_name='record',
            name='symbol_and_doc_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Symbol i numer dowodu'),
        ),
        migrations.AlterField(
            model_name='record',
            name='value_result',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Stan Wartości'),
        ),
    ]