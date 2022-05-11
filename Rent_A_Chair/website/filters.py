import django_filters
from Rent_A_Chair_App.models import Worker
from django_filters import CharFilter


class WorkerFilter (django_filters.FilterSet):
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')

    class Meta:
        model = Worker
        fields = '__all__'
        exclude = ['age']
