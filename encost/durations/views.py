from django.shortcuts import render
import django_filters
from .models import Duration, Client, Equipment, Mode

class DurationFilter(django_filters.FilterSet):
    client = django_filters.ModelChoiceFilter(queryset=Client.objects.all())
    equipment = django_filters.ModelChoiceFilter(queryset=Equipment.objects.all())
    mode = django_filters.ModelChoiceFilter(queryset=Mode.objects.all())
    start = django_filters.DateFilter(field_name='start')
    stop = django_filters.DateFilter(field_name='stop')
    start_hour = django_filters.NumberFilter(field_name='start', lookup_expr='hour')
    stop_hour = django_filters.NumberFilter(field_name='stop', lookup_expr='hour')

    class Meta:
        model = Duration
        fields = ['client', 'equipment', 'mode', 'minutes']

def duration_list(request):
    f = DurationFilter(request.GET, queryset=Duration.objects.all())
    return render(request, 'durations/list.html', {'filter': f})
