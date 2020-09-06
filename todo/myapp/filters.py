from django_filters import FilterSet , CharFilter , DateFilter
from .models import * 

class FinishTodoFilter(FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains' , label="name")
    createAt = DateFilter(field_name="createdAt" , lookup_expr='icontains' , label="Create At")
    endAt = DateFilter(field_name="endAt" , lookup_expr='icontains' , label="End At")

    class Meta:
        model = Todo
        fields = ['tags']
