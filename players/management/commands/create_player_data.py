"""
Creates player stats across many seasons
"""

import datetime
import random

from django.core.management import BaseCommand

from ...factories import (
    PlayerFactory,
    PlayerTeamStintFactory,
    TeamFactory,
)
from ...models import Player, PlayerTeamStint, Team


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            dest="n_players",
            type=int,
            help="Number of players to generate",
            default=100,
        )
        parser.add_argument(
            "-y",
            dest="n_years",
            type=int,
            default=3,
            help="Number of years of data to generate",
        )
        parser.add_argument(
            "-d",
            dest="delete",
            help="Delete existing player data?",
            default=True,
            action="store_true",
        )

    def handle(self, *args, **options):
        if options["delete"] is True:
            Player.objects.filter().delete()
            Team.objects.filter().delete()
            PlayerTeamStint.objects.filter().delete()

        players = [PlayerFactory() for _ in range(options["n_players"])]
        _ = [TeamFactory() for _ in range(30)]

        for year_index in range(options["n_years"]):
            season_start_date = datetime.date(2020, 1, 1) - datetime.timedelta(
                days=year_index * 365
            )

            for player in players:
                if random.randint(0, 10) < 2:
                    player_teams = list(Team.objects.order_by("?")[:2])
                    PlayerTeamStintFactory(
                        player=player,
                        team=player_teams[0],
                        date_joined=season_start_date,
                    )
                    PlayerTeamStintFactory(
                        player=player,
                        team=player_teams[1],
                        date_joined=datetime.date(2020, 6, 1),
                    )
                else:
                    team = Team.objects.order_by("?").first()
                    PlayerTeamStintFactory(
                        player=player, team=team, date_joined=season_start_date
                    )
