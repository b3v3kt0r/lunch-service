from rest_framework import serializers

from menus.models import Restaurant, Menu, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "address"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "restaurant", "date", "items"]


class MenuListSerializer(MenuSerializer):
    restaurant = RestaurantSerializer()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "user", "menu", "date"]
