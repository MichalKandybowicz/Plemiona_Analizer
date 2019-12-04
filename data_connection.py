import csv

TYP_ATTACK = 0
ATTACKER_VILLAGE_CORDS = 1
DATE_AND_TIME = 2
ATTACKER_NICK = 3
DEFENDER_VILLAGE_CORDS = 4
DEFENDER_NICK = 5
WHEN_SENT = 6
DISTANCE = 7
HOW_MANY_ATTACKS = 8


def read_file(PLAYERS_LIST):
    full_data = []
    for nick in PLAYERS_LIST:
        file_directory = "data/csv/" + nick + '.csv'
        with open(file_directory, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f)
            data_from_one_player = list(reader)
            full_data.append(data_from_one_player)

    return full_data


def write_attacks_by_sent_time(list_of_attacks):
    with open("data/rezults/attacks_by_sent_time.txt", "w") as file:
        for attack in list_of_attacks:
            file.write(attack[TYP_ATTACK] + "   " +
                       attack[ATTACKER_VILLAGE_CORDS] + "   " +
                       attack[ATTACKER_NICK] + "   " +
                       attack[DEFENDER_VILLAGE_CORDS] + "   " +
                       attack[DEFENDER_NICK] + "   " +
                       attack[DISTANCE] + "   " +
                       attack[WHEN_SENT] + "   " +
                       attack[HOW_MANY_ATTACKS] + "   " +
                       attack[DATE_AND_TIME] + "   " + "\n")
    file.close()


def write_in_sos_format(list_of_attacks, players_list, sos_format):
    with open("data/rezults/sos_for_all.txt", "w") as sos_for_all:
        for nick in players_list:
            sos_for_all.write(nick + "\n")
            villages_this_player = sos_format[nick]
            for village in villages_this_player:

                sos_for_all.write("\n" + "\t" + village + "\n")
                for attack in list_of_attacks:
                    if attack[DEFENDER_VILLAGE_CORDS] == village and attack[DEFENDER_NICK] == nick:
                        sos_for_all.write("\t" + "\t" + attack[TYP_ATTACK] + "   " +
                                          attack[ATTACKER_VILLAGE_CORDS] + "   " +
                                          attack[ATTACKER_NICK] + "   " +
                                          attack[DISTANCE] + "   " +
                                          attack[WHEN_SENT] + "   " +
                                          attack[HOW_MANY_ATTACKS] + "   " +
                                          attack[DATE_AND_TIME] + "   " + "\n")
    sos_for_all.close()

# TYP_ATTACK = 0
# ATTACKER_VILLAGE_CORDS = 1
# DATE_AND_TIME = 2
# ATTACKER_NICK = 3
# DEFENDER_VILLAGE_CORDS = 4
# DEFENDER_NICK = 5
# WHEN_SENT = 6
# DISTANCE = 7
# HOW_MANY_ATTACKS = 8
