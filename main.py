"""
format for players
    nick 1 (defender)
        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]

        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]

    nick 2 (defender)
        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]

        XXX|YYY - defender village cords
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]
            [ aggressor village, which is the attack from this village , Attack type, aggressor name, attack sent time]


"""

# create list of players who send S.O.S
# txt to csv (delete BB-code, defenders, wall, pop-lvl)
# make data form csv (list of attacks)
# how many attacks from village - list of dict [{xxx|xxx: X},{xxx|xxx: X}]
# calculate distance
# calculate travel time
# seconds to datetime
# calculate when sent
# sort by sent datetime
# list of villages with attacks
# todo


from txt_to_csv import txt_to_csv
import data_connection
import change_data_form
import logic
import filters

TYP_ATTACK = 0
ATTACKER_VILLAGE_CORDS = 1
DATE_AND_TIME = 2
ATTACKER_NICK = 3
DEFENDER_VILLAGE_CORDS = 4
DEFENDER_NICK = 5
WHEN_SENT = 6
DISTANCE = 7
HOW_MANY_ATTACKS = 8

time_s = 5  # odstępy między atakami większe niż podane będą usó∑ane (jako fejki)
how_many = 7  # >= ilości wysłąnych z 1 wioski będą usówane (jako fejki)
min_time = "2021/02/06 07:00:00"  # %Y/%m/%d %H:%M:%S
max_time = "2021/02/06 16:00:00"


def load_and_data_preparation():
    players_list = logic.get_players_list("data/txt/")
    txt_to_csv(players_list)
    data = data_connection.read_file(players_list)
    list_of_attacks = change_data_form.change_format_to_list_of_list(data)
    dict_attacks_from_village = logic.get_how_many_attacks_from_attacker_village(list_of_attacks)
    list_of_attacks = logic.add_sent_time_and_sort_by_this(dict_attacks_from_village, list_of_attacks)
    return list_of_attacks, players_list


def print_stats(stats_all_attacks, removed, stats_attacks_after_filters, stats_how_many_by_name):
    print("wszystkie ataki przed filtrowaniem:", stats_all_attacks)

    print("w sumie uznanych za fejki:", removed)

    print("wszystkie ataki po filtrowaniu:", stats_attacks_after_filters)

    how_many_by_name = dict(sorted(stats_how_many_by_name.items(), key=lambda item: item[1]))
    for i in how_many_by_name:
        print(i, "wysła:", how_many_by_name[i], "ataków")


def main():
    """

    """
    data, players_list = load_and_data_preparation()

    data = logic.add_information_send_no(data)
    stats_all_attacks = len(data)

    sorted_data = logic.sort_by_entry_time(
        data,
    )

    filtered_data, removed = filters.main_filer(
        data=sorted_data, time=time_s, how_many=how_many, min_time=min_time, max_time=max_time
    )

    stats_how_many_by_name = logic.how_many_attacks_by(
        filtered_data
    )

    sos_format = logic.get_sorted_attacks_by_nickname_and_villages_and_sent_time(filtered_data)

    data_connection.write_attacks_by_sent_time(filtered_data)
    data_connection.write_in_sos_format(filtered_data, players_list, sos_format)

    print_stats(stats_all_attacks, removed, len(filtered_data), stats_how_many_by_name)


if __name__ == '__main__':
    main()
