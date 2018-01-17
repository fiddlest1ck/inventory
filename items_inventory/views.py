from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView, ListView
from django.shortcuts import (render, render_to_response, get_object_or_404,
                              redirect)
from django.http import HttpResponseRedirect

from items_inventory.forms import RecordForm
from items_inventory.models import Record, History

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

