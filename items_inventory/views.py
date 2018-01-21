from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView, ListView
from django.shortcuts import (render, render_to_response, get_object_or_404,
                              redirect)
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
import xlwt
from items_inventory.forms import RecordForm
from items_inventory.models import Record, History
from items_inventory.filters import RecordFilter
from items_inventory.templatetags import summary


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'


class RecordsView(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'records/records_list.html'
    context_object_name = 'records'
    paginate_by = 10


class RecordsAddView(LoginRequiredMixin, View):
    template_name = 'records/records_add.html'
    
    def post(self, request, *args, **kwargs):
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save()
            History.objects.create(user=request.user,
                                   operation='Dodano nowy rekord o id {}'.format(record.id))
            return HttpResponseRedirect('/records/add')
        return render_to_response(self.template_name, {'form': form})
    
    def get(self, request, *args, **kwargs):
        form = RecordForm(request.GET)
        return render(request, self.template_name, {'form': form})


class RecordsUploadView(LoginRequiredMixin, View):
    template_name = 'records/records_add.html'

    def post(self, request, pk, *args, **kwargs):
        record = get_object_or_404(Record, pk=pk)
        form = RecordForm(request.POST or None, instance=record)
        if form.is_valid():
            record = form.save()
            History.objects.create(user=request.user,
                                   operation='Zaaktualizowany rekord o id {}'.format(record.id))
        return render(request, self.template_name, {'form': form, 'update': True})

    def get(self, request, pk, *args, **kwargs):
        record = get_object_or_404(Record, pk=pk)
        form = RecordForm(request.GET or None, instance=record)
        return render(request, self.template_name, {'form': form})


class RecordsDeleteView(LoginRequiredMixin, View):
    template_name = 'records/records_add.html'
    
    def get(self, request, pk, *args, **kwargs):
        record = get_object_or_404(Record, pk=pk)
        record.delete()
        History.objects.create(user=request.user,
                               operation='Usunięto rekord o id {}'.format(record.id))
        return redirect('records')


class ReportView(LoginRequiredMixin, View):
    filterset_class = RecordFilter
    template_name = 'records/summary.html'


    def generate_xls(self, name, request, records_filter, columns):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="raport.xls"'
        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet('Raport')
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        row_num = 0
        new_dict = records_filter.data.dict()
        res = {k:v for k,v in new_dict.items() if v is not ''}
        del res['excel']
        if res != {}:
            rows = Record.objects.filter(**res).values_list()
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
            wb.save(response)
            return response
        return render(request, 'records/summary.html', {'filter': records_filter})


    def get(self, request, *args, **kwargs):
        records = Record.objects.all()
        records_filter = RecordFilter(request.GET, queryset=records)
        if request.GET.get('excel'):
            columns = [x.verbose_name for x in Record._meta.fields]

            return self.generate_xls('raport.xls', request, records_filter, columns)
        if request.GET.get('summary'):
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="sumarycznie.xls"'
            wb = xlwt.Workbook(encoding="utf-8")
            ws = wb.add_sheet('Raport')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            row_num = 0
            qdict = QueryDict('', mutable=True)
            font_style = xlwt.XFStyle()
            new_dict = records_filter.data.dict()
            res = {k:v for k,v in new_dict.items() if v is not ''}
            del res['summary']
            value = Record.objects.filter(**res)
            columns = ['Stan ilości', 'Stan Wartości', 'Wartość przychodu',
                       'Wartość rozchodu', 'Cena jednostkowa']
            qdict.update({'Stan ilości': summary.number_result(value),
                     'Stan Wartości': summary.value_result(value),
                     'Wartość przychodu': summary.incoming_value(value),
                     'Wartość rozchodu': summary.outgoing_value(value),
                     'Cena jednostkowa': summary.item_price(value)})
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)           
            for row in qdict:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
            wb.save(response)
            return response
            
        return render(request, 'records/summary.html', {'filter': records_filter})
