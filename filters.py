from datetime import datetime
import logic

# time_s = 5  # odstępy między atakami większe niż podane będą usó∑ane (jako fejki)
# how_many = 10  # >= ilości wysłąnych z 1 wioski będą usówane (jako fejki)
# min_time = "2021/02/06 07:00:00"  # %Y/%m/%d %H:%M:%S
# max_time = "2021/02/06 16:00:00"


def main_filer(data, time, how_many, min_time, max_time):
    how_many_removed = 0

    data, removed = remove_by_time_period(time, data)
    how_many_removed += removed
    print("removed by period time:", removed, "period time:", time)

    data, removed = remove_by_to_many_attacks(data, how_many)
    how_many_removed += removed
    print("removed by too manny attack form 1 village:", removed, "too many is:", how_many)

    data, removed = remove_by_min_max_time(data, min_time, max_time)
    how_many_removed += removed
    print("removed by min/max time:", removed, "min:", min_time, "max:", max_time)

    return data, how_many_removed


def remove_by_min_max_time(data, min_time, max_time):
    removed = 0
    new_data = []
    data_time_min = datetime.strptime(min_time, '%Y/%m/%d %H:%M:%S')
    data_time_max = datetime.strptime(max_time, '%Y/%m/%d %H:%M:%S')

    for i in data:
        attack_data = datetime.strptime(i[2], '%Y/%m/%d %H:%M:%S')
        if data_time_min < attack_data < data_time_max:
            new_data.append(i)
        else:
            removed += 1

    return new_data, removed


def get_list_by_attackers(data):
    new_data = {}
    for i in data:
        if i[3] in new_data:
            new_data[i[3]].append(i)
        else:
            new_data[i[3]] = []
            new_data[i[3]].append(i)
    return new_data


def remove_by_time_period(time, data):
    data = get_list_by_attackers(data)
    filtered_data = []
    out = 0
    for attacker_name in data.keys():
        attacks_list_by_attacker = data[attacker_name]
        for i in range(len(attacks_list_by_attacker)):
            if i >= 1:
                i_send_time = datetime.strptime(attacks_list_by_attacker[i][6], '%Y/%m/%d %H:%M:%S')
                i_m1_send_time = datetime.strptime(attacks_list_by_attacker[i - 1][6], '%Y/%m/%d %H:%M:%S')
                diff = i_send_time - i_m1_send_time
                if diff.seconds > time:
                    filtered_data.append(attacks_list_by_attacker[i])
                else:
                    out += 1

            elif i+1 < len(attacks_list_by_attacker):
                i_send_time = datetime.strptime(attacks_list_by_attacker[i][6], '%Y/%m/%d %H:%M:%S')
                i_p1_send_time = datetime.strptime(attacks_list_by_attacker[i+1][6], '%Y/%m/%d %H:%M:%S')
                diff = i_p1_send_time - i_send_time
                if diff.seconds > time:
                    filtered_data.append(attacks_list_by_attacker[i])
                else:
                    out += 1
            else:
                filtered_data.append(attacks_list_by_attacker[i])
    return filtered_data, out


def remove_by_to_many_attacks(data, how_many):
    new_data = []
    how_many_removed = 0
    for i in data:

        if (len(i[8]) == 3) and (int(i[8][2]) >= how_many):
            how_many_removed += 1

        elif (len(i[8]) == 5) and (int(i[8][3:]) >= how_many):
            how_many_removed += 1

        else:
            new_data.append(i)

    return new_data, how_many_removed

