import constants
import copy

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

x = players

#cleaning data: removing 'inches' from Height strings
for char in x:
    #char['height'].replace(' inches', '')
    char['height'] = char['height'].replace(' inches', '')
    char['height'] = int(char['height'])



#cleaning data: Setting Height to integer values:
#char['height'] = int(char['height'])

 
#for i in range(0, len(y)): 
 #   y[i] = int(y[i])
    


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

#while option1 == '2':
#    quit

total_players = int(len(players) / len(teams))




p = 0
player_names = []

h = 0
heights_list = []

while option2 == '1':
    #print('\nTeam: {} Stats'.format(teams[0]))
    #print('\nTotal Players: {}'.format(total_players))
    player_names.append(players[p]['name'])
    #print('\nPlayers on team:\n {}'.format(player_names[-1]))
    p += 1
    if p==6:
        break
    heights_list.append(players[h]['height'])
    h +=1
    if h==6:
        break

    
if option2 == '1':  
    print('\nTeam: {} Stats:'.format(teams[0]))
    print('\nTotal Players: {}'.format(total_players))
    print('\nPlayers on team:\n {}'.format(player_names))
    print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
    print('heights_list: {}'.format(heights_list))

#print(char['height']) ======================== 41
    
#print(heights_list) =================== 41.41.14.41....



p=6
h=6
while option2 == '2':
    player_names.append(players[p]['name'])
    heights_list.append(players[h]['height'])

    p += 1
    if p==12:
        break
    h +=1
    if h==12:
        break

    

if option2 == '2':
    print('\nTeam: {} Stats:'.format(teams[1]))
    print('\nTotal Players: {}'.format(total_players))
    print('\nPlayers on team:\n {}'.format(player_names))
    print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
    print('heights_list: {}'.format(heights_list))



p=12
h=12
while option2 == '3':
    player_names.append(players[p]['name'])
    heights_list.append(players[h]['height'])

    p += 1
    if p==18:
        break
    h +=1
    if h==18:
        break

if option2 == '3':
    print('\nTeam: {} Stats:'.format(teams[2]))
    print('\nTotal Players: {}'.format(total_players))
    print('\nPlayers on team:\n {}'.format(player_names))
    print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
    print('heights_list: {}'.format(heights_list))



print('Press ENTER to continue...')
