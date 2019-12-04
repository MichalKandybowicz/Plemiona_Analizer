# ATTACK_TYPE
# ATTACKER_VILLAGE
# ATTACK_TIME
# ATTACKER_NICK
# DEFENDER_VILLAGE
# DEFENDER_NICK


def change_format_to_list_of_list(all_players_data):
    new_all_players_data = []

    for one_player_data in all_players_data:
        players_list = []
        cord_list = []
        for i in range(len(one_player_data)):

            if i == 0:
                players_list.append(one_player_data[i][0])
            elif (len(one_player_data[i]) == 1) and (i > 0):
                cord_list.append(one_player_data[i][0])

            else:
                one_attack = [one_player_data[i][0],  # ATTACK_TYPE
                              one_player_data[i][1],  # ATTACKER_VILLAGE
                              one_player_data[i][2],  # ATTACK_TIME
                              one_player_data[i][3],  # ATTACKER_NICK
                              cord_list[-1],          # DEFENDER_VILLAGE
                              players_list[-1]   # DEFENDER_NICK
                              ]
                new_all_players_data.append(one_attack)

    return new_all_players_data
