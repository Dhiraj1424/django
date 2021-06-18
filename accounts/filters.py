import django_filters
from .models import*
from django_filters import DateFilter


class OrderFilter(django_filters.FilterSet):
#kun field anusar search garni ho field name ma teai hunuparxa ra tyo field 
#field model ma pani huna parxa
    start_data = DateFilter(field_name="date_created", lookup_expr='gte')
    end_data = DateFilter(field_name="date_created", lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        # mathi all vayepani yesle tala ko command run garxa override garxa
        # customer search garne thau ma talako field dekidina
        #  but mathi field name gareko chi dekinaxa
        exclude = ['customer', 'date_created']
