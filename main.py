import time
import random

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