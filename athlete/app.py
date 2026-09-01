""" Main app for the Athletes module."""
from Game import Game
from Team import Team
from Sport import Sport
from Athlete import Athlete
import json

def load_json_file(file_path):
    """ Loads a JSON file."""
    data = None
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def convert_json_to_teams(json_data):
    """ Converts JSON data."""
    teams = []
    for team_data in json_data:
        team_name = team_data['name']
        sport_name = team_data['sport']['name']
        sport_league = team_data['sport']['league']
        sport_num_players = team_data['sport']['num_players']
        print(team_name,sport_name,sport_league,sport_num_players)
    
def main():
    """ Main function."""
    tournament_data = load_json_file('/media/jesus/UNIDAD USB/Desarrollo de sistemas 4/trabajos en clase/athlete/tournament.json')
    print("Tournament:", tournament_data)

if __name__ == "__main__":
    main()