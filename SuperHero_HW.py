import requests
from pprint import pprint

Hero_URL = "https://superheroapi.com/api/2619421814940190/"


def search_intelligence_get(search_name):
    list_intelligence = list()
    for heroes in search_name:
        url = Hero_URL + "search/" + heroes
        response_character = requests.get(url, timeout=2).json()["results"][0]
        list_intelligence.append({'id': response_character["id"],
                                  'name': response_character["name"],
                                  'intelligence': int(response_character["powerstats"]["intelligence"])})
    return list_intelligence


if __name__ == '__main__':
    search_hero = ['Hulk', 'Captain America', 'Thanos']
    res = search_intelligence_get(search_hero)
    pprint(res)

    max_intelligence = {'id': 0, 'name': 'none', 'intelligence': 0}
    for super_hero in res:
        if max_intelligence['intelligence'] < super_hero['intelligence']:
            max_intelligence = super_hero

    print(f'Герой {max_intelligence["name"]} с максимальным уровнем intelligence = {max_intelligence["intelligence"]}')
