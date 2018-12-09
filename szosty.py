samochod=['opel','polonez','reanult']

print(', '.join(samochod))

arr='a,b,c,d,e'.split(',')
print(arr)



#11. dwie listy


samochody=['syrena','polonez']
ilosc=[3,5]

for idx in range(len(samochody)):
    print('idx: '+str(idx)+': '+samochody[idx])
    print(samochody[idx]+' ma ilosc drzwi '+str(ilosc[idx]))

print(samochod[0]+' '+samochod[2])

#12. koszyk

produkt=['mleko','maslo','bulka']
cena=[100,120,150,200]

suma=0

for c in cena:
    suma=suma+c

if len(produkt)>=3:
    print('Udane zakupy')
    suma=suma-(suma*0.15)

print('Do zaplaty: {0}'.format(suma))
