from django.contrib import admin

from menus.models import (
    Menu,
    Restaurant,
    Vote
)

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Vote)
