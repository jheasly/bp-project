from django.db import models


class Player(models.Model):
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name_first} {self.name_last}"


class Team(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class PlayerTeamStint(models.Model):
    """Collects stats from a player-team stint"""

    player = models.ForeignKey(Player, related_name="seasons", on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team, related_name="players", on_delete=models.SET_NULL, null=True
    )

    # dates wherein given player played for given team
    date_joined = models.DateField()

    b_ab = models.PositiveIntegerField()
    b_pa = models.PositiveIntegerField()
    b_hits = models.PositiveIntegerField()
    b_1b = models.PositiveIntegerField()
    b_2b = models.PositiveIntegerField()
    b_3b = models.PositiveIntegerField()
    b_hr = models.PositiveIntegerField()
    b_rbi = models.PositiveIntegerField()
    b_runs = models.PositiveIntegerField()
    b_sb = models.PositiveIntegerField()
    b_bb = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.player} - {self.team}"
