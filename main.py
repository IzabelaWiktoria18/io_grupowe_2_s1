def waluta_str_na_dict(s):

    waluta_dict = {
        "galeon": 0,
        "sykl": 0,
        "knut": 0
    }
    
    czesci = s.split()

    for i in range(0, len(czesci), 2):
        wartosc = int(czesci[i])
        jednostka = czesci[i+1]
        
     
        if jednostka.startswith('g'):
            waluta_dict['galeon'] = wartosc
        elif jednostka.startswith('s'):
            waluta_dict['sykl'] = wartosc
        elif jednostka.startswith('k'):
            waluta_dict['knut'] = wartosc
    
    return waluta_dict

# Przykładowe użycie
print(waluta_str_na_dict("18 knut"))


print(waluta_str_na_dict("19 galeon 2 sykl 16 knut"))