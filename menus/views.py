from rest_framework import viewsets

from menus.models import (
    Restaurant,
    Menu,
    Vote
)
from menus.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    VoteSerializer
)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
