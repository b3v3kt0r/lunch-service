from rest_framework import viewsets

from menus.models import (
    Restaurant,
    Menu,
    Vote
)
from menus.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    VoteSerializer, MenuListSerializer, MenuRetrieveSerializer
)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MenuListSerializer
        elif self.action == "retrieve":
            return MenuRetrieveSerializer
        return MenuSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return self.queryset.select_related()
        return queryset


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
