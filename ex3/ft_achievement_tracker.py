import random


def get_player_achievements() -> set[str]:
    achievements = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
        ]
    return set(random.sample(achievements,
                             random.randint(2, len(achievements))))


def player_generator() -> None:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    alice = get_player_achievements()
    bob = get_player_achievements()
    charlie = get_player_achievements()
    dylan = get_player_achievements()
    sets = [alice, bob, charlie, dylan]
    distinct: set[str] = set()
    common: set[str] = alice
    i = 0
    while i < len(players):
        print(f"Player {players[i]}: {sets[i]}")
        distinct = distinct.union(sets[i])
        common = common.intersection(sets[i])
        i += 1
    print(f"\nAll distinct achievements: {distinct}\n")
    print(f"Common achievements: {common}\n")
    i = 0
    while i < len(players):
        others: set[str] = set()
        j = 0
        while j < len(sets):
            if j != i:
                others = others.union(sets[j])
            j += 1
        print(f"Only {players[i]} has: {sets[i] - others}")
        i += 1
    print("")
    i = 0
    while i < len(players):
        print(f"{players[i]} is missing: {distinct - sets[i]}")
        i += 1


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player_generator()


# ##Alternative
# import random


# def get_player_achievements() -> set[str]:
#     achievements = [
#         'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
#         'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
#         'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
#         'Boss Slayer'
#     ]
#     return set(random.sample(achievements,
#                              random.randint(1, len(achievements))))


# def player_generator() -> None:
#     alice = get_player_achievements()
#     bob = get_player_achievements()
#     charlie = get_player_achievements()
#     dylan = get_player_achievements()

#     print(f"Player Alice: {alice}")
#     print(f"Player Bob: {bob}")
#     print(f"Player Charlie: {charlie}")
#     print(f"Player Dylan: {dylan}")

#     distinct = alice.union(bob).union(charlie).union(dylan)
#     common = alice.intersection(bob).intersection(charlie)
#     common = common.intersection(dylan)

#     print(f"\nAll distinct achievements: {distinct}\n")
#     if len(common) == 0:
#         print("Common achievements: None\n")
#     else:
#         print(f"Common achievements: {common}\n")

#     print(f"Only Alice has: {alice - bob.union(charlie).union(dylan)}")
#     print(f"Only Bob has: {bob - alice.union(charlie).union(dylan)}")
#     print(f"Only Charlie has: {charlie - alice.union(bob).union(dylan)}")
#     print(f"Only Dylan has: {dylan - alice.union(bob).union(charlie)}")

#     print(f"\nAlice is missing: {distinct - alice}")
#     print(f"Bob is missing: {distinct - bob}")
#     print(f"Charlie is missing: {distinct - charlie}")
#     print(f"Dylan is missing: {distinct - dylan}")


# if __name__ == "__main__":
#     print("=== Achievement Tracker System ===\n")
#     player_generator()
