pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

def who_has_wooden_leg(pirates):
    wooden_legged = []
    for pirate in pirates:
        if pirate["has_wooden_leg"] == True and pirate["gold"] >= 15:
            wooden_legged.append(pirate["Name"])
    return wooden_legged

print(who_has_wooden_leg(pirates))