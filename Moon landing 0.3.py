#Moon landing
print ('Nacházíte se v přistávacím modulu lodi.')
print ('Vašim cílem je přistát na měsíci!')
print ('Porouchal se vám ale počítač pro řízení přistání')
print ('Takže musíš přistát manuálně')
print ('Nastavuj každé kolo výkon přistávacího motoru,')
print ('a bezpečně přistaň.')
r0 = 50
r1 = 8
r2 = 90
r3 = 36
r4 = 8000
while r0 >= 0:
    motorová_páka = input ('Nastav výkon motoru 1-100% ')
    r6 = 1.62 - ((int(motorová_páka) * int(r3) / int(r4)) * 10)
    r0 = r0 - r1 - (r6 / 2)
    r1 = r1 + r6
    r2 = int(r2) - (int(motorová_páka) * int(r3) / 240)
    print ('Jsi ve výšce')
    print (r0)
    print ('Klesáš rychlostí')
    print (r1)
    print ('Zbývá ti paliva')
    print (r2)
    if r2 <= 0:
        r3 = 0
        r2 = 0
    if r0 <= 0:
        print ('Přistál jsi rychlostí')
        print (r1)
        print('Zbylo ti paliva')
        print (r2)
        if r1 >= 10:
            print ('Měli jsme tě rádi')
        elif r1 < 10 and r1 > 8:
            print ('Přistáli jste v pořádku ale, bylo to jen tak tak.')
        elif r1 < 8 and r1 > 6:
            print ('Poměrně dobré přistání, ale máš ještě co pilovat.')
        elif r1 < 6 and r1 > 4:
            print ('Hele, na to že nejsi kosmonaut je to dobrý.')
        elif r1 < 4 and r1 > 2: 
            print ('Přistáli jste v pořádku ale, bylo to jen tak tak.')
        elif r1 < 2 and r1 > 0: 
            print ('Mám vážné pochybnosti, že nejsi kosmonaut. Obstál jsi výborně.')
