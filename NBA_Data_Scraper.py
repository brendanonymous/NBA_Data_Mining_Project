from bs4 import BeautifulSoup
import requests


CONST_TEAMS_URL = 'http://www.espn.com/nba/standings/_/group/league'


# scrape team names, return dict e.g. {rank:team name}
def scrape_teams_and_rankings():
    response = requests.get(CONST_TEAMS_URL)

    try:
        response.raise_for_status()
    except:
        print('404 Error: CONST_TEAMS_URL does not exist!\nEnding program...')
        exit()

    teams = {}

    soup = BeautifulSoup(response.text, 'lxml')
    team_names = soup.find_all(class_='hide-mobile', recursive=True)

    for index, child in enumerate(team_names):
        teams[index] = child.text

    return teams


if __name__ == '__main__':
    current_teams = scrape_teams_and_rankings()
    print(current_teams[0]) # showing that it worked