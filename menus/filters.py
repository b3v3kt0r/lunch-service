import django_filters
from menus.models import Restaurant


class RestaurantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Restaurant
        fields = ["name"]
