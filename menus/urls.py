from django.urls import path, include
from rest_framework import routers

from menus.views import (
    MenuViewSet,
    RestaurantViewSet,
    VoteViewSet
)


app_name = "menus"

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet)
router.register("votes", VoteViewSet)

urlpatterns = [path("", include(router.urls))]
