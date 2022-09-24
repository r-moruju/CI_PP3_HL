import requests


def get_country_population(country):
    """
    Get specific country population from the API
    """
    url = "https://world-population.p.rapidapi.com/population"

    querystring = {"country_name": country}

    headers = {
        "X-RapidAPI-Key": "934924768dmshb3321c772dbb901p1afa28jsna764ae2d255d",
        "X-RapidAPI-Host": "world-population.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers,
                                params=querystring, timeout=10)

    return response.json()["body"]["population"]


def get_countries_list():
    """
    Create a list with word's countries from the API
    """
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
        print(f"{self.name} has a population of {self.population}")


def country_class(country):
    """
    Creates country class and access his method
    """
    population = get_country_population(country)
    new_country_class = Country(country, population)
    print(type(new_country_class.population))
    new_country_class.describe()


new_country = countries_list[0]

country_class(new_country)
