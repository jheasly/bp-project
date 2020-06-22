from django.contrib import admin

from .models import Player, Team, PlayerTeamStint


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("full_name", )

    def full_name(self, obj):
        return str(obj)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PlayerTeamStint)
class PlayerTeamStintAdmin(admin.ModelAdmin):
    list_display = ("player", "team", "date_joined")
