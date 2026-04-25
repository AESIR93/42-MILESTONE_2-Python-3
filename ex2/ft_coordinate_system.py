import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        args = raw.split(",")
        if len(args) != 3:
            print("Invalid syntax")
            continue
        result: tuple[float, ...] = ()
        valid = True
        i = 0
        while i < len(args):
            try:
                result = result + (float(args[i]),)
            except ValueError as e:
                print(f"Error on parameter '{args[i].strip()}': {e}")
                valid = False
                break
            i += 1
        if valid and len(result) == 3:
            return result


def get_distance(pos1: tuple[float, ...], pos2: tuple[float, ...]) -> float:
    return round(math.sqrt((pos2[0] - pos1[0]) ** 2
                           + (pos2[1] - pos1[1]) ** 2
                           + (pos2[2] - pos1[2]) ** 2), 4)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coords_1 = get_player_pos()
    print(f"Got a first tuple: {coords_1}")
    print(f"It  includes: X={coords_1[0]}, Y={coords_1[1]}, Z={coords_1[2]}")
    print(f"Distance to center: {get_distance(coords_1, (0.0, 0.0, 0.0))}\n")
    print("Get a second set of coordinates")
    coords_2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{get_distance(coords_1, coords_2)}\n")
