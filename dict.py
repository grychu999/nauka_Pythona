#13

samolot={'name':'boeing',
        'przebieg':10000,
        'type':'pasazerski'}

print(samolot['name'])
print(samolot['przebieg'])


for key,value in samolot.iteritems():
    print("{0}:{1}".format(key,value))

for key in samolot:
    print('{0}:{1}'.format(key,samolot[key]))


# koszyk ze slownikiem

koszyk=[
    {'name':'mleko','cena':12.5},
    {'name':'ser','cena':4.0},
    {'name':'konsola gier','cena':114.0}
]

suma=0
for i in range(len(koszyk)):
    suma=suma+float(koszyk[i]['cena'])
print(suma)

#mleko i ser - 10% znizki

bylo_mleko=False
byl_ser=False

suma=0

for poz in koszyk:
    suma=suma+poz['cena']
    nazwa_prod=poz['name']
    if nazwa_prod=='mleko':
        bylo_mleko=True
    if nazwa_prod=='ser':
        byl_ser=True

if bylo_mleko and byl_ser:
    print('ZNIZKAAA')
    suma=suma-suma*0.1
print(suma)

#14

produkty={'S1222':'sukienka trojkat',
            'P1222':'spodnie krata',
            'X212':'konsola do gier'}

igla='X2'

if igla in produkty:
    print("znalazlem {0}".format(igla))
else:
    print("Brak w magazynie {0}".format(igla))
igla='X2'

if igla in produkty:
    print("znalazlem {0}".format(igla))
else:
    print("Brak w magazynie {0}".format(igla))


produkty={'S1222':'sukienka trojkat',
            'P1222':'spodnie krata',
            'X212':'konsola do gier'}


igla='spodnie krata'

for value in produkty.iteritems():
    if produkty[value]==igla:
        print("znalazlem")
else:
    print("Brak w magazynie {0}".format(igla))
