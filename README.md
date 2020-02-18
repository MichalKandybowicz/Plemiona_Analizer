## Table of contents
* [General info](#general-info)
* [Key features](#Key-features)
* [Technologies](#technologies)
* [ToDo](#Todo)
* [How use it](#How-use-it)

## General info
A project to facilitate the analysis of upcoming attacks, a useful tool for the defense coordinator.
He will get many useful information to determine
- who is the target
- what area is mainly under attack
- where the fake attacks go
- where additional troops will be needed

## Key features
- determining the time of sending the army by the enemy
- displaying the number of attacks from a given village
- ordering attacks to be sent
	
## Technologies
Project is created with:
- Python version: 3.7
	
## Todo
- adding information via a dedicated website (with register/login system)
- storing information in a database
- displaying information on the website

## How use it


Output format (for players), have many information about attacks.
```
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
```


1. paste into the txt file named as your nickname S.O.S content 
2. put this file together with other tribe players' files in "data / txt"
3. run main.py

```
NICKNAME.txt

[b]Wioska:[/b] [coord]516|650[/coord]
[b]Poziom muru:[/b] 20
[b]Poparcie:[/b] 100

[b]Obrońca:[/b]  0  0  7998  0  80  2000  244  0  322  140  0  4  0

    [command]attack[/command] Taran [coord]588|650[/coord] --> Czas przybycia: 17.12.19 07:20:59:960 [player]ElSamag[/player]
    [command]attack[/command] Taran [coord]593|603[/coord] --> Czas przybycia: 17.12.19 08:42:06:474 [player]ElSamag[/player]
    [command]attack[/command] Taran [coord]591|625[/coord] --> Czas przybycia: 17.12.19 10:36:07:907 [player]ElSamag[/player]
  
[b]Wioska:[/b] [coord]531|619[/coord]
[b]Poziom muru:[/b] 20
[b]Poparcie:[/b] 100

[b]Obrońca:[/b]  27039  14694  0  7453  1949  0  0  3629  0  25  0  0  0

    [command]attack[/command] Taran [coord]547|646[/coord] --> Czas przybycia: 17.12.19 07:23:50:195 [player]Vazqu[/player]
    [command]attack[/command] Taran [coord]598|559[/coord] --> Czas przybycia: 17.12.19 07:36:55:734 [player]Pawwe[/player]
    [command]attack[/command] Taran [coord]598|559[/coord] --> Czas przybycia: 17.12.19 07:37:27:722 [player]Pawwe[/player]
    [command]attack[/command] Taran [coord]594|580[/coord] --> Czas przybycia: 17.12.19 07:44:29:349 [player]ElSamag[/player]
  
```




