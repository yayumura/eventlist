from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Event

class ListEventView(ListView):
    template_name = 'eventapp/event_list.html'
    model = Event
    # context_object_name = 'AAA' # オブジェクト名をobject_listからAAAに変更

class DetailEventView(DetailView):
    template_name = 'eventapp/event_detail.html'
    model = Event
    # context_object_name = 'AAA' # オブジェクト名をobjectからAAAに変更

class CreateEventView(CreateView):
    template_name = 'eventapp/event_create.html'
    model = Event
    fields = ('title', 'date', 'link', 'category')
    success_url = reverse_lazy('list-event')

class DeleteEventView(DeleteView):
    template_name = 'eventapp/event_delete.html'
    model = Event
    success_url = reverse_lazy('list-event')

class UpdateBookView(UpdateView):
    template_name = 'eventapp/event_update.html'
    model = Event
    fields = ('title', 'date', 'link', 'category')
    success_url = reverse_lazy('list-event')
