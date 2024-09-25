from datetime import date

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from menus.filters import RestaurantFilter
from menus.models import (
    Restaurant,
    Menu,
    Vote
)
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


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()

    @action(detail=False, methods=["get"])
    def current_day(self, request):
        today = date.today()
        menu = Menu.objects.filter(date=today).first()
        if menu:
            serializer = self.get_serializer(menu)
            return Response(serializer.data)
        return Response({"detail": "No menu for today."}, status=404)

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

    @action(detail=False, methods=["get"])
    def results(self, request):
        today = date.today()
        favorite_menu = (
            Vote.objects.filter(date=today)
            .values("menu")
            .annotate(count=Count("id"))
            .order_by("-count")
            .first()
        )

        if favorite_menu:
            return Response(favorite_menu)
        return Response({"detail": "No votes found for today."}, status=404)

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
