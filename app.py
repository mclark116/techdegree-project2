import constants
import copy

players = copy.deepcopy(constants.PLAYERS)

teams = copy.deepcopy(constants.TEAMS)

height_integer = []

experience = []

player_names = []

num_on_teams = len(players)/len(teams)

panthers = []
bandits = []
warriors = []

team_list = [panthers, bandits, warriors]



def start_game():
    print('BASKETBALL TEAM STATS TOOL')
    print('\n'*1)
    print('-'*4 + 'MENU' + '-'*4) 
    print('\n'*1)
def main_menu():
    print(''' Here are your choices:  
      1) Display Team Stats
      2) Quit
          ''')
    
    while True:
        try:
            entry = int(input('\nPlease enter your choice (1 or 2) >'))
        except ValueError:
            print("Oh no! Please enter a valid choice.")
            continue
        if entry == 1:
            print('\nHere are your team choices:')
            for index, item in enumerate(teams, 1):
                print(f'{index}) {item}')
            break
        elif entry == 2:
            print('Goodbye!')
            quit()
        else:
            print('Please enter a valid choice')
            continue
    while True:
        try:
            team_choice = int(input('\nWhich team would you like to view? '))
        except ValueError:
            print('Oh no! Please select a number 1-3')
            continue
        if team_choice == 1 or team_choice == 2 or team_choice ==3:
            team_name = teams[team_choice-1]
            print('\nTeam: {} Stats'.format(team_name))
            print('-'*20)             
            print('Total Players: {} '.format(len(team_list[team_choice-1])))
            print('\nPlayers on team:')
            print(', '.join(team_list[team_choice-1]))
        else:
            print('\nOh no! Please enter a valid option.')
            continue
        while True:
            try:
                continue_game = input('\nWould you like to continue? Y/N ')
            except ValueError:
                print('Oh no! Please enter Y or N.')
            if continue_game.lower() == 'y':
                print('\n')
                main_menu()
            elif continue_game.lower() == 'n':
                print('\nCome again soon!')
                quit()
            else:
                print('Oh no! Please enter Y or N.')
        
def clean_data():
    for player in players:
        player_height = player['height'].split(' ')
        height_integer.append(int(player_height[0]))
        experience = player['experience']
        if experience == 'YES':
            experience = True
        if experience == 'NO':
            experience = False
    
def balance_team():
    for player in players:
        player_names = player['name']
        if len(panthers) < num_on_teams:
            panthers.append(player_names)
        elif len(bandits) < num_on_teams:
            bandits.append(player_names)
        elif len(warriors) < num_on_teams:
            warriors.append(player_names)
    
if __name__=='__main__':
    balance_team()
    clean_data()
    start_game()
    main_menu()