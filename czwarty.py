produkt='mleko'
suma=200

if suma>=100 and suma<200:
    print('Promocja 30%!')
    suma = suma - suma*0.3
elif suma>=200:
    print('Promocja 35%!')
    suma = suma - suma*0.35
else:
    print('Bez promocji!')

print('Do zaplacenia '+str(suma))
