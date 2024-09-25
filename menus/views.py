from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from menus.filters import RestaurantFilter
from menus.models import (
    Restaurant,
    Menu,
    Vote
)
from menus.permissions import IsAdminAllORIsAuthenticatedReadOnly
from menus.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    MenuListSerializer,
    MenuRetrieveSerializer,
    VoteSerializer,
    VoteListRetrieveSerializer
)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RestaurantFilter
    permission_classes = [IsAdminAllORIsAuthenticatedReadOnly]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = [IsAdminAllORIsAuthenticatedReadOnly]

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
    permission_classes = [IsAdminAllORIsAuthenticatedReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VoteListRetrieveSerializer
        return VoteSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return self.queryset.select_related()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
