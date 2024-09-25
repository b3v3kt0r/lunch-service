from rest_framework import viewsets

from menus.models import (
    Restaurant,
    Menu,
    Vote
)
from menus.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    VoteSerializer, MenuListSerializer
)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MenuListSerializer
        return MenuSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return self.queryset.select_related()
        return queryset


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
