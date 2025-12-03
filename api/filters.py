import django_filters
from app.models import Item

class CustomFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name='product', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description',lookup_expr='iexact')
    id= django_filters.RangeFilter(field_name='id')
     
    class Meta:
        model = Item
        fields = ['product','description','id']