"""
This module works with the API to get Country population
by using requests library, and creates Class instances for each country
"""
import requests


def get_country_population(country: str) -> int:
    """
    Get specific country population from the API
    @param country(string): A country name generated by the API
    """

    # Code snippet from https://rapidapi.com/aldair.sr99/api/world-population/
    url = "https://world-population.p.rapidapi.com/population"

    querystring = {"country_name": country}

    headers = {
        "X-RapidAPI-Key": "934924768dmshb3321c772dbb901p1afa28jsna764ae2d255d",
        "X-RapidAPI-Host": "world-population.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers,
                                params=querystring, timeout=10)

    return response.json()["body"]["population"]


def get_countries_list() -> list:
    """
    Create a list with word's countries from the API
    """

    # Code snippet from https://rapidapi.com/aldair.sr99/api/world-population/
    url = "https://world-population.p.rapidapi.com/allcountriesname"

    headers = {
        "X-RapidAPI-Key": "934924768dmshb3321c772dbb901p1afa28jsna764ae2d255d",
        "X-RapidAPI-Host": "world-population.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, timeout=10)

    countries_lst = response.json()["body"]["countries"]
    return countries_lst


countries_list = get_countries_list()


class Country():
    """
    Creates a country class instance
    """
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def describe(self):
        """
        Print country population
        """
        print(f"{self.name} has a population of {self.population}".center(80))


def country_class(country: str) -> int:
    """
    Creates country class and access the population
    @param country(string): A country name to create a country class instance
    """
    if country == "India":
        population = 1407563842
    else:
        population = get_country_population(country)
    new_country_class = Country(country, population)
    return new_country_class.population


def country_population(country: str):
    """
    Creates country class and access the method
    @param country(string): A country name to create a country class instance
    """
    if country == "India":
        population = 1407563842
    else:
        population = get_country_population(country)
    new_country_class = Country(country, population)
    return new_country_class.describe()
