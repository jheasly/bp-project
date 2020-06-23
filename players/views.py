from django.views.generic import ListView

from .models import PlayerTeamStint

# Create your views here.
class StatsSeasonsTeamsListView(ListView):
    def get_queryset(self):
        return PlayerTeamStint.objects.filter(date_joined__contains='2020')
        # return PlayerTeamStint.objects.select_related('team').select_related('player').filter(date_joined__contains='2020')

