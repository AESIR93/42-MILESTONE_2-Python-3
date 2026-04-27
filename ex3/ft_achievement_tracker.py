import random


def get_player_achievements() -> set[str]:
    achievements = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
        ]
    return set(random.sample(achievements,
                             random.randint(1, len(achievements))))


def player_generator(number: int) -> None:
    players = ["Alice", "Bob", "Charlie", "Dylan",
               "Eddy", "Francis", "Gabriel"]
    distinct: set[str] = set()
    common: set[str] = set()
    temp: set
    i = 0
    while i < number:
        temp = get_player_achievements()
        distinct = distinct | temp
        start = True
        if start:
            common = temp
            start = False
        common &= temp
        print(f"Player: {players[i]}: {temp}")
        i += 1
    print(f"\nAll distinct achievements: {distinct}\n")
    print(f"Common achievements: {common} ")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player_generator(4)
