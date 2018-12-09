marka='Peugeot'
ilosc_drzwi=5
pojemnosc=1.3
marka_up=marka.upper()
marka_down=marka_up.lower()
marka_down=str.lower(marka_up)
print('Samochod '+marka+' ma '+str(ilosc_drzwi)+' drzwi')
print(marka_up)
print('Pojemnosc po zmianach: '+str(pojemnosc*2))
print(marka_down)
print(marka.swapcase())
print(len(marka))

if ilosc_drzwi >3:
    print('Duzy samochod')
else:
    print('Maly')

if marka.startswith('Pe'):
    print('Jest to niestety '+marka)
