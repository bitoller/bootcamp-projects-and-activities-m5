from datetime import datetime
from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError


def data_processing(national_team):
    first_cup_formatted = national_team.get("first_cup")
    titles = int(national_team.get("titles"))
    first_cup = datetime.strptime(first_cup_formatted, "%Y-%m-%d").date()

    if titles < 0:
        raise NegativeTitlesError()

    if first_cup.year < 1930 or (first_cup.year - 1930) % 4 != 0:
        raise InvalidYearCupError()

    expected_titles = (datetime.now().year - first_cup.year) // 4

    if titles > expected_titles:
        raise ImpossibleTitlesError()
