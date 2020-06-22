import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from .models import Player, PlayerTeamStint, Team


class PlayerFactory(DjangoModelFactory):
    name_first = factory.Faker("first_name")
    name_last = factory.Faker("last_name")

    class Meta:
        model = Player


class TeamFactory(DjangoModelFactory):
    name = factory.Faker("company")

    class Meta:
        model = Team


class PlayerTeamStintFactory(DjangoModelFactory):
    player = factory.SubFactory(PlayerFactory)
    team = factory.SubFactory(TeamFactory)

    # batting stats
    b_ab = factory.fuzzy.FuzzyInteger(low=0, high=500)
    b_pa = factory.fuzzy.FuzzyInteger(low=0, high=700)
    b_hits = factory.fuzzy.FuzzyInteger(low=0, high=300)
    b_1b = factory.fuzzy.FuzzyInteger(low=0, high=100)
    b_2b = factory.fuzzy.FuzzyInteger(low=0, high=50)
    b_3b = factory.fuzzy.FuzzyInteger(low=0, high=50)
    b_hr = factory.fuzzy.FuzzyInteger(low=0, high=100)
    b_rbi = factory.fuzzy.FuzzyInteger(low=0, high=200)
    b_runs = factory.fuzzy.FuzzyInteger(low=0, high=200)
    b_sb = factory.fuzzy.FuzzyInteger(low=0, high=100)
    b_bb = factory.fuzzy.FuzzyInteger(low=0, high=100)

    class Meta:
        model = PlayerTeamStint
