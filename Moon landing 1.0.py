#! python3
# Moon landing, by foglar (inspired by the game Moon Lander by ABC Computer Games)
from rich import console

c = console.Console()

c.print('  ********     --------     --------   ----    ----    ----            ------    ----    ---- ----------   --------  ----    ---- ------------ ', style='white')
c.print(' ----------   **********   **********  *****   ****    ****           ********   *****   **** ************ ********  *****   **** ************ ', style='white')
c.print('************ ----    ---- ----    ---- ------  ----    ----          ----------  ------  ---- --        --   ----    ------  ---- ----         ', style='white')
c.print('---  --  --- ***      *** ***      *** ************    ****         ****    **** ************ **        **   ****    ************ ****  ****** ', style='white')
c.print('***  **  *** ---      --- ---      --- ------------    ----         ------------ ------------ --        --   ----    ------------ ----  ------ ', style='white')
c.print('---  --  --- ****    **** ****    **** ****  ******    ************ ************ ****  ****** **        **   ****    ****  ****** ****    **** ', style='white')
c.print('***  **  ***  ----------   ----------  ----   -----    ------------ ----    ---- ----   ----- ------------ --------  ----   ----- ------------ ', style='white')
c.print('---      ---   ********     ********   ****    ****    ************ ****    **** ****    **** **********   ********  ****    **** ************ ', style='white')


c.print('Nacházíte se v přistávacím modulu lodi appolo...', style='green')
c.print('Vašim cílem je přistát na Měsíci!', style='green')
c.print('Porouchal se vám ale počítač pro řízení přistání...', style='green')
c.print('...takže musíš přistát manuálně', style='green')
c.print('Nastavuj každé kolo výkon přistávacího motoru,', style='green')
c.print('a bezpečně přistaň.', style='green')

r0 = 50
r1 = 8
r2 = 90
r3 = 36
r4 = 8000

def drawMoon():
    print('''                   _  _     ____________.--.
                  |\|_|//_.-"" .'    \   /|  |
                  |.-"""-.|   /       \_/ |  |
                  \  ||  /| __\_____________ |
                  _\_||_/_| .-""            ""-.  __
                .' '.    \//                    ".\/
                ||   '. >()_                     |()<
                ||__.-' |/\ \                    |/\\
                   |   / "|  \__________________/.""
                  /   //  | / \ "-.__________/  /\\
               ___|__/_|__|/___\___".______//__/__\\
              /|\     [____________] \__/         |\\
             //\ \     |  |=====| |   /\\\\         |\\\\
            // |\ \    |  |=====| |   | \\\\        | \\\\        ____...____....----
          .//__| \ \   |  |=====| |   | |\\\\       |--\\\\---""""     .            ..
_____....-//___|  \_\  |  |=====| |   |_|_\\\\      |___\\\\    .                 ...'
 .      .//-.__|_______|__|_____|_|_____[__\\\\_____|__.-\\\\      .     .    ...::
        //        //        /          \ `-_\\\\/         \\\\          .....:::
  -... //     .  / /       /____________\    \\\\       .  \ \     .            .
      //   .. .-/_/-.                 .       \\\\        .-\_\-.                 .
     / /      '-----'           .             \ \      '._____.'         .
  .-/_/-.         .                          .-\_\-.                          ...
 '._____.'                            .     '._____.'                       .....
        .                                                             ...... ..
    .            .                  .                        .
   ...                    .                      .                       .      .
        ....     .                       .                    ....
 JRO      ......           . ..                       ......'
             .......             '...              ....
                                   ''''''      .              .''')

while r0 >= 0:
    try:
        c.print('Nastav výkon motoru 1-100%:', style='cyan')
        motorová_páka = input('> ')
        
        while True:
            try:
                motorová_páka = int(motorová_páka)
                break
            except ValueError:
                if not motorová_páka.isnumeric():
                    c.print('Musíš zadat číslo od 0 - 100!', style='red')
                    motorová_páka = input('> ')
                elif motorová_páka >= 100:
                    motorová_páka = int(100)
                elif motorová_páka <= 0:
                    motorová_páka = int(0)
                else:
                    motorová_páka = int(motorová_páka)

        
        
        r6 = 1.62 - ((int(motorová_páka) * int(r3) / int(r4)) * 10)
        r0 = r0 - r1 - (r6 / 2)
        r1 = r1 + r6
        r2 = int(r2) - (int(motorová_páka) * int(r3) / 240)

        c.print(f'Jsi ve výšce [bold red]{r0}[/bold red]', style='cyan')
        c.print(f'Klesáš rychlostí [bold red]{r1}[/bold red]', style='cyan')
        c.print(f'Zbývá ti paliva [bold red]{r2}[bold red]', style='cyan')

        if r2 <= 0:
            r3 = 0
            r2 = 0

        if r0 <= 0:
            c.print(f'Přistál jsi rychlostí [bold red]{r1}[/bold red]', style='blue')
            c.print(f'Zbylo ti paliva [bold red]{r2}[/bold red]', style='blue')
            if r1 >= 10:
                c.print('Měli jsme tě rádi', style='red')
            elif r1 < 10 and r1 > 8:
                c.print('Přistáli jste v pořádku ale, bylo to jen tak tak.', style='red')
            elif r1 < 8 and r1 > 6:
                c.print('Poměrně dobré přistání, ale máš ještě co pilovat.', style='yellow')
            elif r1 < 6 and r1 > 4:
                c.print('Hele, na to že nejsi kosmonaut je to dobrý.', style='yellow')
            elif r1 < 4 and r1 > 2: 
                c.print('Přistáli jste v pořádku ale, bylo to jen tak tak.', style='green')
            elif r1 < 2 and r1 > 0: 
                c.print('Mám vážné pochybnosti, že nejsi kosmonaut. Obstál jsi výborně.', style='green')
                drawMoon()

    except KeyboardInterrupt:
        c.print('Ukončuji program...', style='red')
        exit()
