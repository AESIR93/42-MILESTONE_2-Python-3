import sys


def process_scores(input: list[int]) -> None:
    player_cnt = len(input)
    max_score = max(input)
    min_score = min(input)
    total = sum(input)
    print(f"Scores processed: {input}")
    print(f"Total players: {player_cnt}")
    print(f"Total score: {total}")
    print(f"Average score: {total/player_cnt}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}\n")


if __name__ == "__main__":
    args = sys.argv[1:]
    scores: list[int] = []
    print("\n=== Player Score Analytics ===")

    i = 0
    while i < len(args):
        try:
            scores = scores + [int(args[i])]
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
        i += 1

    if len(scores) == 0:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...\n")
    else:
        process_scores(scores)
