from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Team
from django.forms.models import model_to_dict
from exceptions import InvalidYearCupError
from exceptions import NegativeTitlesError
from exceptions import ImpossibleTitlesError
from utils import data_processing


class TeamsView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)
        return Response(teams_dict)

    def post(self, request):
        payload = request.data
        if payload.get("id"):
            payload.pop("id")
        try:
            data_processing(payload)
            team = Team(**payload)
            team.save()
            return Response(model_to_dict(team), 201)
        except (
            NegativeTitlesError,
            InvalidYearCupError,
            ImpossibleTitlesError,
        ) as err:
            return Response({"error": err.message}, 400)


class TeamsInfoView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team_dict = model_to_dict(team)
        return Response(team_dict)

    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        for key, value in request.data.items():
            setattr(team, key, value)
        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict, 200)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team.delete()
        return Response(status=204)
