#Lists allow you to have re-adjustable "lists" of data with no pre-defined length
#example of lists using games that would be played at EVO
saturday_game_list = ['SSBM', 'USFIV', 'MVC3', 'SSB4']
sunday_game_list = ['MKX', 'Tekken7', 'Killer Instinct', 'P4AU']
master_game_list = [saturday_game_list, sunday_game_list]

#utilizing indexes
print 'First game played at EVO:', saturday_game_list[0]
print '\nLast game played at EVO:', sunday_game_list[3]
print '\nSaturday lineup: ', saturday_game_list
print '\nSunday lineup: ', sunday_game_list
print '\nAll games in order', master_game_list

#using build in list fuctions
saturday_game_list.append('GGXrd')

print '\n' * 2, master_game_list

master_game_list.insert(0,'Saturday')
master_game_list.insert(2, 'Sunday')

print '\n', master_game_list

master_game_list.remove("Saturday")
master_game_list.remove("Sunday")

print '\n', master_game_list

master_game_list2 = saturday_game_list + sunday_game_list

print '\n', master_game_list2

print '\n', len(master_game_list2), 'Games in list'