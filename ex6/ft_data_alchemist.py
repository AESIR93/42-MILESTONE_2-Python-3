import random


def player_list() -> None:
    p_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
              'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {p_list}")

    capitalize = [player.capitalize() for player in p_list]
    print(f"New list with all names capitalized: {capitalize}")
    capd_only = [player for player in p_list if player == player.capitalize()]
    print(f"New list of capitalized names only: {capd_only}")

    score_dict = {player: random.randint(0, 500) for player in capitalize}
    print(f"Score dict: {score_dict}")

    average = round(sum(score_dict[p] for p in score_dict)/len(score_dict), 2)
    print(f"Score average is {average}")

    high_score_dict = {player: score_dict[player] for player in
                       capitalize if score_dict[player] > average}
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    player_list()
    print()
