from django.test import TestCase
from django.contrib.auth import get_user_model
from menus.models import Restaurant, Menu, Vote
from datetime import date

User = get_user_model()


class RestaurantModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Test St"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.restaurant), self.restaurant.name)


class MenuModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Test St"
        )
        self.menu = Menu.objects.create(
            restaurant=self.restaurant, date=date.today(), items="Test items"
        )

    def test_string_representation(self):
        self.assertEqual(
            str(self.menu), f"Menu: {self.menu.items} for '{self.menu.restaurant}'"
        )


class VoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Test St"
        )
        self.menu = Menu.objects.create(
            restaurant=self.restaurant, date=date.today(), items="Test items"
        )
        self.vote = Vote.objects.create(
            user=self.user, menu=self.menu, date=date.today()
        )

    def test_vote_creation(self):
        self.assertEqual(self.vote.user.username, "testuser")
        self.assertEqual(self.vote.menu.items, "Test items")
