
import csv
import re


def txt_to_csv(PLAYERS_LIST):
    for nick in PLAYERS_LIST:
        with open('data/txt/' + nick + '.txt', 'r') as infile, open('data/csv/' + nick + '.csv', 'w') as outfile:
            line_stripped = (line.strip() for line in infile)
            line_nick = [nick]
            lines = [line_nick]

            for line in line_stripped:

                line = line.replace("[b]Wioska:[/b] ", "")
                line = line.replace("[b]Poparcie:[/b] 100", "")

                if "[b]Po" in line:
                    line = ""
                elif "[b]Ob" in line:
                    line = ""

                elif len(line) > 25:
#[command]attack[/command] Taran [coord]430|469[/coord] --> Czas przybycia: 24.09.20 15:32:54:881 [player]Lord Sebus
# Trzeci[/player]
                    line = line.replace("nd] [co", "nd] nieOpisany [co")
                    line = line.replace("[command]attack[/command] ", "")
                    line = line.replace(" [coord]", "!@!")
                    line = line.replace("[/coord] --> Czas przybycia: ", "!@!")
                    line = line.replace(" [player]", "!@!")
                    line = line.replace("[/player]", "")
                    line = line.split("!@!")

                    # line = [item[::-1] for item in line[::-1].split('-', 4)][::-1]
                    lines.append(line)

                elif len(line) > 5:
                    line = line.replace("[coord]", "")
                    line = line.replace("[/coord]", "")
                    lines.append([line])

            writer = csv.writer(outfile)
            writer.writerows(lines)