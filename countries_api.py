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

    response = requests.request("GET", url, headers=headers, params=querystring)

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

    response = requests.request("GET", url, headers=headers)

    countries_lst = response.json()["body"]["countries"]
    return countries_lst


countries_list = get_countries_list()

print(countries_list)