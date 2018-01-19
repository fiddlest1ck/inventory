from django.db import models


class Record(models.Model):
    in_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Nr kolejny przychodu')
    out_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Nr kolejny rozchodu')
    in_date = models.DateField(blank=True, null=True, verbose_name='Data przychodu i względnie rozchodu')
    symbol_and_doc_number = models.CharField(blank=True, max_length=255, null=True, verbose_name='Symbol i numer dowodu')
    stock_item_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Numer fabryczny przedmiotu (obiektu)')
    item_name_description_state = models.TextField(blank=True, null=True, verbose_name='Nazwa przedmiotu (obiektu) jego opis i stan')
    item_price = models.FloatField(blank=True, null=True, verbose_name='Cena jednostkowa')
    number_of_incoming = models.PositiveIntegerField(blank=True, null=True, default=1, verbose_name='Ilość przychodu')
    number_of_outgoing = models.PositiveIntegerField(blank=True, null=True, default=1, verbose_name='Ilość rozchodu')
    number_result = models.IntegerField(blank=True, null=True, default=0, verbose_name='Stan Ilości')
    incoming_value = models.CharField(blank=True, max_length=255, default='1', verbose_name='Wartość przychodu')
    outgoing_value = models.CharField(blank=True, max_length=255, default='1', verbose_name='Wartość rozchodu')
    value_result = models.CharField(blank=True, max_length=255, default='0', verbose_name='Stan Wartości')
    next_number = models.IntegerField(blank=True, null=True, verbose_name='Przeciwstawny numer kolejny')
    additionals = models.TextField(blank=True, null=True, verbose_name='UWAGI (co do miejsca znajdowania sie przedmiotu i inne)')


class History(models.Model):
    user = models.ForeignKey('auth.User', null=True, blank=True, verbose_name='Użytkownik', on_delete='ignore')
    operation = models.CharField(max_length=255, null=True, blank=True, verbose_name='Operacja')
    old_value = models.CharField(max_length=255, null=True, blank=True, verbose_name='wcześniejsza wartość')
    new_value = models.CharField(max_length=255, null=True, blank=True, verbose_name='nowa wartość')
    
