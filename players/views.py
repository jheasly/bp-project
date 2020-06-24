from django.views.generic import ListView

from .models import PlayerTeamStint

#TODO: Handle multiple years

# Create your views here.
class StatsSeasonsTeamsListView(ListView):
    def get_queryset(self):
        # returned in 50ms, 41 queries
        # return PlayerTeamStint.objects.filter(date_joined__contains='2020')

        # select_related magic: returned in 10ms, 1 query
        return PlayerTeamStint.objects.select_related('team').select_related('player').filter(date_joined__contains='2020')

    def get_context_data(self, **kwargs):
        '''Hard wire the season in a kinda elegant way'''
        context = super().get_context_data(**kwargs)
        context['season'] = '2020'
        return context
