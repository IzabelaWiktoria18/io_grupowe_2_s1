import main;

def test_wybierz_sowe_zwroc_koszt(self):
        self.assertEqual(wybierz_sowe_zwroc_koszt(False, 'lokalna', 'list', 'wyjec'), {"galeon" : 0,"sykl" : 0, "knut" : 13})
        self.assertEqual(wybierz_sowe_zwroc_koszt(True, 'krajowa', 'list', 'list gończy'), {'galeon': 0, 'sykl': 1, 'knut': 19})



