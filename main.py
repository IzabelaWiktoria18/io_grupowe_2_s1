import time
import random


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

