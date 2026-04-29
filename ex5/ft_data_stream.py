import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    p_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
              'Gregory', 'john', 'kevin', 'Liam']
    a_list = ['run', 'eat', 'sleep', 'grab', 'move',
              'climb', 'swim', 'use', 'release']
    while True:
        yield (random.choice(p_list), random.choice(a_list))


def consume_event(event_list: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list):
        yield event_list.pop(random.randrange(len(event_list)))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    i = 0
    while i < 1000:
        player, action = next(event)
        print(f"Event {i}: Player {player} did action {action}")
        i += 1
    print()
    event_list: list[tuple[str, str]] = []
    i = 0
    while i < 10:
        event_list = event_list + [next(event)]
        i += 1
    print(f"Built list of 10 events: {event_list}\n")

    c_event = consume_event(event_list)
    for n in c_event:
        print(f"Got event from list: {n}")
        print(f"Remains in list: {event_list}")
