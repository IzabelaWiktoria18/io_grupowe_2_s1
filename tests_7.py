def test_waluta_dict_na_str():
    # Test przypadek 1: Słownik zawiera tylko niezerowe wartości
    assert waluta_dict_na_str({"galeon": 1, "sykl": 2, "knut": 3}) == "1 galeon 2 sykl 3 knut"
    
    # Test przypadek 2: Słownik zawiera mieszane wartości zerowe i niezerowe
    assert waluta_dict_na_str({"galeon": 0, "sykl": 2, "knut": 0}) == "2 sykl"
    
    # Test przypadek 3: Słownik zawiera tylko wartości zerowe
    assert waluta_dict_na_str({"galeon": 0, "sykl": 0, "knut": 0}) == ""
    
    # Test przypadek 4: Słownik zawiera różne wartości walut
    assert waluta_dict_na_str({"galeon": 3, "sykl": 0, "knut": 15}) == "3 galeon 15 knut"
    
    # Test przypadek 5: Pusty słownik
    assert waluta_dict_na_str({}) == ""

# Wywołanie funkcji testującej
test_waluta_dict_na_str()

