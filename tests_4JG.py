import main;

def wybierz_sowe_zwroc_koszt():
    assert main.wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec') == wynik, "niepoprawny wynik"


test_wybierz_sowe_zwroc_koszt(False, main.Odleglosc.LOKALNA, main.TypPaczki.LIST, main.SpecjalnaPaczka.WYJEC, {"galeon": 0, "sykl": 0, "knut": 6})
test_wybierz_sowe_zwroc_koszt(True, main.Odleglosc.DALEKOBIEZNA, main.TypPaczki.PACZKA, main.SpecjalnaPaczka.NIE_DOTYCZY, {"galeon": 0, "sykl": 2, "knut": 8})



