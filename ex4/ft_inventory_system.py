import sys


def parse_input(my_dict: dict[str, int]) -> None:
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        parts = args[i].split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{args[i]}'")
        else:
            try:
                if parts[0] in my_dict:
                    print(f"Redundant item '{parts[0]}' - discarding")
                else:
                    my_dict[parts[0]] = int(parts[1])
            except ValueError as e:
                print(f"Quantity error for '{parts[0]}': {e}")
        i += 1


def show_stats(my_dict: dict[str, int]) -> None:
    if len(my_dict) == 0:
        print("No items in inventory")
        return
    keys = list(my_dict.keys())
    values = list(my_dict.values())
    print(f"Got inventory: {my_dict}")
    print(f"Item list: {keys}")
    print(f"Total quantity of the {len(my_dict)} items:"
          f" {sum(my_dict.values())}")
    percent: list[float] = [0.0] * len(keys)
    max_idx = 0
    min_idx = 0
    total = sum(values)
    i = 0
    while i < len(keys):
        percent[i] = round((values[i]/total*100), 1)
        print(f"Item {keys[i]} represents {percent[i]}%")
        if percent[i] > percent[max_idx]:
            max_idx = i
        if percent[i] < percent[min_idx]:
            min_idx = i
        i += 1
    print(f"Item most abundant: {keys[max_idx]} "
          f"with quantity {values[max_idx]}")
    print(f"Item least abundant: {keys[min_idx]} "
          f"with quantity {values[min_idx]}")


def update_inventory(my_dict: dict[str, int]) -> None:
    my_dict.update({'magic_item': 1})
    print(f"Updated inventory: {my_dict}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    my_dict: dict[str, int] = {}
    parse_input(my_dict)
    show_stats(my_dict)
    update_inventory(my_dict)
