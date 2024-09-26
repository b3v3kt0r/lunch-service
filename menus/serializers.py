from rest_framework import serializers

from menus.models import (
    Restaurant,
    Menu,
    Vote
)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "address"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "restaurant", "date", "items"]


class MenuRetrieveSerializer(MenuSerializer):
    restaurant = RestaurantSerializer()


class MenuListSerializer(MenuSerializer):
    restaurant = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "menu", "date", "user"]
        read_only_fields = ["id", "user"]


class VoteListRetrieveSerializer(serializers.ModelSerializer):
    menu = serializers.SlugRelatedField(
        slug_field="items",
        read_only=True
    )
    restaurant = serializers.CharField(source="menu.restaurant.name")

    class Meta:
        model = Vote
        fields = ["id", "menu", "restaurant", "date"]
