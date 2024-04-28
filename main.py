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