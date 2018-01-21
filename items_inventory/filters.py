from items_inventory.models import Record
from django import forms
import django_filters


class RecordFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = ['symbol_and_doc_number', 'in_date', 'out_date',]

    symbol_and_doc_number = django_filters.CharFilter(lookup_expr='icontains')
    in_date__year__gt = django_filters.NumberFilter(field_name='in_date', widget=forms.DateInput(),
                                            lookup_expr='in_date__year__gt')
    in_date__year__lt = django_filters.NumberFilter(field_name='in_date', widget=forms.DateInput(),
                                            lookup_expr='in_date__year__lt')
    out_date__year__gt = django_filters.NumberFilter(field_name='out_date', widget=forms.DateInput(),
                                             lookup_expr='out_date__year__gt')
    out_date__year__lt = django_filters.NumberFilter(field_name='out_date', widget=forms.DateInput(),
                                             lookup_expr='out_date__year__lt')
    in_date__month__gt = django_filters.NumberFilter(field_name='in_date', widget=forms.DateInput(),
                                            lookup_expr='in_date__month__gt')
    in_date__month__lt = django_filters.NumberFilter(field_name='in_date', widget=forms.DateInput(),
                                            lookup_expr='in_date__month__lt')
    out_date__month__gt = django_filters.NumberFilter(field_name='out_date', widget=forms.DateInput(),
                                             lookup_expr='out_date__month__gt')
    out_date__month__lt = django_filters.NumberFilter(field_name='out_date', widget=forms.DateInput(),
                                             lookup_expr='out_date__month__lt')
    
