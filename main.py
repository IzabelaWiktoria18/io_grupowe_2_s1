def licz_sume(adict):
    galeon_coins = adict["galeon"]
    sykl_coins = adict["sykl"]
    knut_coins = adict["knut"]
    all_galeons = sum(galeon_coins)
    all_sykls = sum(sykl_coins)
    all_knuts = sum(knut_coins)
    if all_knuts > 20:
        to_add = int(all_knuts/21)
        all_sykls += to_add
        all_knuts -= to_add * 21
    if all_sykls > 16:
        to_add = int(all_sykls/17)
        all_galeons += to_add
        all_sykls -= to_add * 17
    new_dict = {"galeon": all_galeons, "sykl" : all_sykls, "knut": all_knuts}
    return new_dict
"""
print(licz_sume({
    "galeon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
}))
"""