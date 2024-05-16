import csv

def waluta_dict_na_str(waluta_dict):
    result = []
    for klucz, wartosc in waluta_dict.items():
        if wartosc != 0:
            result.append(f"{wartosc} {klucz}")
    return ' '.join(result)

def wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna):
    # Przykładowa funkcja do obliczania kosztu
    koszt = {"galeon": 0, "sykl": 0, "knut": 0}
    
    # Dodajemy przykładowe koszty na podstawie odległości
    if odleglosc == "lokalna":
        koszt["knut"] += 5
    elif odleglosc == "krajowa":
        koszt["sykl"] += 3
    elif odleglosc == "dalekobieżna":
        koszt["galeon"] += 1
    
    # Dodajemy przykładowe koszty na podstawie typu
    if typ == "list":
        koszt["knut"] += 2
    elif typ == "paczka":
        koszt["sykl"] += 1
    
    # Dodajemy przykładowe koszty na podstawie specjalnego typu
    if specjalna == "wyjec":
        koszt["knut"] += 10
    elif specjalna == "list gończy":
        koszt["galeon"] += 5
    
    return koszt

def nadaj_sowe(adresat, tresc_wiadomosci, potwierdzenie_odbioru, odleglosc, typ, specjalna):
    koszt = wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna)
    koszt_str = waluta_dict_na_str(koszt)
    potwierdzenie_odbioru_str = "TAK" if potwierdzenie_odbioru else "NIE"
    
    with open('poczta_nadania_lista.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([adresat, tresc_wiadomosci, koszt_str, potwierdzenie_odbioru_str])

# Przykładowe użycie funkcji
nadaj_sowe(
    adresat="Harry Potter",
    tresc_wiadomosci="Spotkajmy się jutro o 17:00",
    potwierdzenie_odbioru=True,
    odleglosc="lokalna",
    typ="list",
    specjalna="nie dotyczy"
)


