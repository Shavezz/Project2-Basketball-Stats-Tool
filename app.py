import constants
import copy


teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)


x = players

#cleaning data: removing 'inches' from Height strings

for char in x:
    char['height'] = char['height'].replace(' inches', '')
    char['height'] = int(char['height'])


for char in x:
    char['guardians'] = char['guardians'].replace(" and ", ', ')




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



p = 0
player_names = []

h = 0
heights_list = []

e=0
players_experience = []

g=0
guardians_list = []

while option2 == '1':
    player_names.append(players[p]['name'])
    p += 1
    if p==7:
        break
    heights_list.append(players[h]['height'])
    h +=1
    if h==7:
        break
    players_experience.append(players[e]['experience'])
    e += 1
    if e==7:
        break
    guardians_list.append(players[g]['guardians'])
    g += 1
    if g==7:
        break
                          
   
if option2 == '1':  
    print('\nTeam: {} Stats:'.format(teams[0]))
    print('heights_list: {}'.format(heights_list))
    print('\nTotal Players: {}'.format(total_players))
    print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
    print('\nTotal inexperienced: {}'. format(len(players_experience) - players_experience.count(True)))
    print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
    print('\nPlayers on team:\n {}'.format(player_names))
    print('\nGuardians: {}'.format(guardians_list))




p = 6
h = 6
e = 6
g = 6
while option2 == '2':
    player_names.append(players[p]['name'])
    p += 1
    if p==13:
        break
    heights_list.append(players[h]['height'])
    h +=1
    if h==13:
        break
    players_experience.append(players[e]['experience'])
    e += 1
    if e==13:
        break
    guardians_list.append(players[g]['guardians'])
    g += 1
    if g==13:
        break   
    

if option2 == '2':
    print('\nTeam: {} Stats:'.format(teams[0]))
    print('heights_list: {}'.format(heights_list))
    print('\nTotal Players: {}'.format(total_players))
    print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
    print('\nTotal inexperienced: {}'. format(len(players_experience) - players_experience.count(True)))
    print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
    print('\nPlayers on team:\n {}'.format(player_names))
    print('\nGuardians: {}'.format(guardians_list))




p = 12
h = 12
e = 12
g = 12
while option2 == '3':
    player_names.append(players[p]['name'])
    p += 1
    if p==18:
        break
    heights_list.append(players[h]['height'])
    h +=1
    if h==19:
        break
    players_experience.append(players[e]['experience'])
    e += 1
    if e==19:
        break
    guardians_list.append(players[g]['guardians'])
    g += 1
    if g==19:
        break  

if option2 == '3':
    print('\nTeam: {} Stats:'.format(teams[0]))
    print('heights_list: {}'.format(heights_list))
    print('\nTotal Players: {}'.format(total_players))
    print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
    print('\nTotal inexperienced: {}'. format(len(players_experience) - players_experience.count(True)))
    print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
    print('\nPlayers on team:\n {}'.format(player_names))
    print('\nGuardians: {}'.format(guardians_list))





