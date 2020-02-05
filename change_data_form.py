ATTACK_TYPE = 0
ATTACKER_VILLAGE = 1
ATTACK_TIME = 2
ATTACKER_NICK = 3
DEFENDER_VILLAGE = -1  # last element form defender village list
DEFENDER_NICK = -1  # last element frm defender nick list


def change_format_to_list_of_list(data_dict_form):
    data_list_form = []

    for one_player_data in data_dict_form:
        players_list = []
        cord_list = []
        for i in range(len(one_player_data)):

            if i == 0:
                players_list.append(one_player_data[i][0])
            elif (len(one_player_data[i]) == 1) and (i > 0):
                cord_list.append(one_player_data[i][0])

            else:
                one_attack = [one_player_data[i][ATTACK_TYPE],  # ATTACK_TYPE
                              one_player_data[i][ATTACKER_VILLAGE],  # ATTACKER_VILLAGE
                              one_player_data[i][ATTACK_TIME],  # ATTACK_TIME
                              one_player_data[i][ATTACKER_NICK],  # ATTACKER_NICK
                              cord_list[DEFENDER_VILLAGE],          # DEFENDER_VILLAGE
                              players_list[DEFENDER_NICK]        # DEFENDER_NICK
                              ]
                data_list_form.append(one_attack)

    return data_list_form
