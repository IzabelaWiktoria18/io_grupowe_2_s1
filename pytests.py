from zad3 import licz_sume

test_dict = {
    "galeon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
}

desired_dict = {
    "galeon" : 12,
    "sykl" : 0,
    "knut" : 14
}
assert licz_sume(test_dict) == desired_dict, "Nie dziala"