
import constants
import copy

if __name__ == '__main__':

    teams = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)

    x = players

    #cleaning data: removing 'inches' from Height strings

    for char in x:
        char['height'] = char['height'].replace(' inches', '')
        char['height'] = int(char['height'])



    for char in x:
        char['guardians'] = char['guardians'].replace(" and ", ', ')





    #for key, value in x.items():
        #''.join(value)


    #cleaning data: Setting Experience to Boolean values:

    for player in players:
        if player['experience'] == 'YES':
            player['experience'] = True

        else:
            player['experience'] = False
            


    print('\nHere are your choices: \n1) Display Team Stats \n2) Quit')

    option1 = input('\nEnter an option > ')

    if option1 == '1':
        for index, i in enumerate(teams, 1):
            print (index, i)
    else:
        exit()
            

    option2 = input('\nEnter an option > ')

    total_players = int(len(players) / len(teams))


    player_names = []

    heights_list = []

    players_experience = []

    g=0
    guardians_list = []

    while option2 == '1':
        player_names.append(players[g]['name'])
       
       
        heights_list.append(players[g]['height'])
      
        players_experience.append(players[g]['experience'])
      
        guardians_list.append(players[g]['guardians'])
        g += 1
        if g==6:
            break
                              
       
    if option2 == '1':  
        print('\nTeam: {} Stats:'.format(teams[0]))
        print('heights_list: {}'.format(heights_list))
        print('\nTotal Players: {}'.format(total_players))
        print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
        print('\nTotal inexperienced: {}'. format(len(players_experience) - players_experience.count(True)))
        print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
        print('\nPlayers on team:\n {}'.format(', '.join(player_names)))
        print('\nGuardians:\n {}'.format(', '.join(guardians_list)))




    g = 6
    while option2 == '2':
        player_names.append(players[g]['name'])
     
        heights_list.append(players[g]['height'])

        players_experience.append(players[g]['experience'])

        guardians_list.append(players[g]['guardians'])
        g += 1
        if g==12:
            break   
        

    if option2 == '2':
        print('\nTeam: {} Stats:'.format(teams[1]))
        print('heights_list: {}'.format(heights_list))
        print('\nTotal Players: {}'.format(total_players))
        print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
        print('\nTotal inexperienced: {}'. format(len(players_experience) - players_experience.count(True)))
        print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
        print('\nPlayers on team:\n {}'.format(', '.join(player_names)))
        print('\nGuardians:\n {}'.format(', '.join(guardians_list)))




    g = 12
    while option2 == '3':
        player_names.append(players[g]['name'])

        heights_list.append(players[g]['height'])

        players_experience.append(players[g]['experience'])

        guardians_list.append(players[g]['guardians'])
        g += 1
        if g==18:
            break  

    if option2 == '3':
        print('\nTeam: {} Stats:'.format(teams[2]))
        print('heights_list: {}'.format(heights_list))
        print('\nTotal Players: {}'.format(total_players))
        print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
        print('\nTotal inexperienced: {}'. format(len(players_experience) - players_experience.count(True)))
        print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
        print('\nPlayers on team:\n {}'.format(', '.join(player_names)))
        print('\nGuardians:\n {}'.format(', '.join(guardians_list)))


