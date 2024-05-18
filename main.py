import csv
import datetime
import time
import random

def wyslij_sowe(adresat, tresc):
    return random.choice([True, False])

def poczta_wyslij_sowy(sciezka_do_pliku):
    # Odczytaj dane z pliku csv
    with open(sciezka_do_pliku, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    wyniki = []
    for row in rows:
        adresat = row['adresat']
        tresc = row['tresc wiadomosci']
        koszt_przesylki = float(row['koszt przesylki'])
        potwierdzenie_odbioru = row['potwierdzenie odbioru']
        
        # Wyślij sowę
        sowa_doleciala = wyslij_sowe(adresat, tresc)
        
        # Określenie rzeczywistego kosztu
        if sowa_doleciala:
            rzeczywisty_koszt = koszt_przesylki
        else:
            if potwierdzenie_odbioru == 'TAK':
                rzeczywisty_koszt = 0
            else:
                rzeczywisty_koszt = koszt_przesylki
        
        wyniki.append({
            'adresat': adresat,
            'tresc wiadomosci': tresc,
            'koszt przesylki': koszt_przesylki,
            'potwierdzenie odbioru': potwierdzenie_odbioru,
            'rzeczywisty koszt': rzeczywisty_koszt
        })

    # Generowanie nazwy pliku wyjściowego
    dzisiaj = datetime.datetime.now()
    nazwa_pliku_wyjsciowego = dzisiaj.strftime("output_sowy_z_poczty_%d_%m_%Y.csv")

    # Zapisanie wyników do pliku csv
    with open(nazwa_pliku_wyjsciowego, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['adresat', 'tresc wiadomosci', 'koszt przesylki', 'potwierdzenie odbioru', 'rzeczywisty koszt']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for wynik in wyniki:
            writer.writerow(wynik)

    print(f'Wyniki zapisano do pliku: {nazwa_pliku_wyjsciowego}')

def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    # Słownik kosztów podstawowych
    koszty_podstawowe = {
        "lokalna": {"list": 2, "paczka": 7},
        "krajowa": {"list": 12, "paczka": 23},  # 1 sykl 2 knuty = 23 knuty
        "dalekobiezna": {"list": 20, "paczka": 43}  # 2 sykle 1 knut = 43 knuty
    }

    # Uzyskujemy koszt podstawowy na podstawie odległości i typu
    koszt = koszty_podstawowe[odleglosc][typ]

    # Dodajemy koszt za potwierdzenie odbioru
    if potwierdzenie_odbioru:
        koszt += 7  # 7 knutów za potwierdzenie

    # Dodajemy koszt za opcje specjalne
    if specjalna == "wyjec":
        koszt += 4  # 4 knuty za wyjec
    elif specjalna == "list gonczy":
        koszt += 22  # 1 sykl = 21 knutów, więc 21+1=22 knuty

    # Przeliczenie kosztu na monety
    sykl_na_knut = 21
    galeon_na_sykl = 17

    # Obliczamy ilość galeonów, sykli, knutów z sumy knutów
    galeony = koszt // (galeon_na_sykl * sykl_na_knut)
    reszta_po_galeonach = koszt % (galeon_na_sykl * sykl_na_knut)

    sykli = reszta_po_galeonach // sykl_na_knut
    reszta_po_syklach = reszta_po_galeonach % sykl_na_knut

    knuty = reszta_po_syklach

    # Zwracamy wynik jako słownik
    return {
        "galeon": galeony,
        "sykl": sykli,
        "knut": knuty
    }


# Przykładowe wywołanie funkcji
wynik = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')
print(wynik)
# Oczekiwany wynik: {'galeon': 0, 'sykl': 0, 'knut': 13}

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

def waluta_dict_na_str(waluta_dict):
    # Tworzymy listę do przechowywania części wyniku
    result = []
    
    # Iterujemy przez słownik
    for klucz, wartosc in waluta_dict.items():
        # Pomijamy wartości zerowe
        if wartosc != 0:
            # Dodajemy odpowiednią parę klucz-wartość do listy wynikowej
            result.append(f"{wartosc} {klucz}")
    
    # Łączymy elementy listy w jeden ciąg znaków oddzielone spacją
    return ' '.join(result)

# Przykładowe użycie:
print(waluta_dict_na_str({
    "galeon": 0,
    "sykl": 0,
    "knut": 13
}))  # Wyjście: "13 knut"

print(waluta_dict_na_str({
    "galeon": 17,
    "sykl": 2,
    "knut": 13
}))  # Wyjście: "17 galeon 2 sykl 13 knut"

def wyslij_sowe():
    adresat = input("Podaj adresata: ")
    tresc = input("Podaj treść listu: ")
    
    print(f"Wysyłanie sowy do: {adresat}")
    time.sleep(1)  # Odczekaj 1 sekundę

    # Zrandomizuj sukces lub porażkę (90% sukcesu, 10% porażki)
    if random.random() < 0.9:
        print("Sowa wysłana pomyślnie.")
        return True
    else:
        print("Wystąpił błąd podczas wysyłania sowy.")
        return False

# Przykładowe użycie funkcji
wynik = wyslij_sowe()
print("Wynik operacji:", wynik)
