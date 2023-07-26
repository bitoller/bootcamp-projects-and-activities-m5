from django.urls import path
from .views import TeamsView, TeamsInfoView


urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<team_id>/", TeamsInfoView.as_view())
]
