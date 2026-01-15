#!/usr/bin/env python3


import time


def ft_event_generator(limit):
    players = ["alice", "bob", "charlie", "david"]

    for i in range(1, limit + 1):
        p_name = players[i % len(players)]
        p_level = ((i * 13) % 15) + 1
        if i % 11 == 0:
            p_action = "found treasure"
        elif i % 7 == 0:
            p_action = "leveled up"
        else:
            p_action = "killed monster"
        yield {
            "id": i,
            "player": p_name,
            "level": p_level,
            "action": p_action
        }


def ft_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def ft_primes(n):
    found = 0
    num = 2
    while found < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            found += 1
        num += 1


def main():
    print("=== Game Data Stream Processor ===\n")

    stream_limit = 1000000
    print(f"Processing {stream_limit} game events...")
    total_processed = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    start_time = time.time()

    for event in ft_event_generator(stream_limit):
        total_processed += 1
#       display first 3 events
        if event.get("id") <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
#       analytics
        if event.get('level') > 10:
            high_level_count += 1
        if event.get('action') == "found treasure":
            treasure_count += 1
        if event.get('action') == "leveled up":
            levelup_count += 1
    end_time = time.time()
    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {stream_limit}")
    print(f"High-level players (+10): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n Generator Demonstration ===")
    fib_gen = ft_fibonacci(10)
    fib_results = []
    for _ in range(10):
        fib_results.append(str(next(fib_gen)))
    print(f"Fibonacci sequence first (10) : {', '.join(fib_results)}")
#   without for
    prime_gen = ft_primes(5)
    p1 = next(prime_gen)
    p2 = next(prime_gen)
    p3 = next(prime_gen)
    p4 = next(prime_gen)
    p5 = next(prime_gen)
    print(f"Prime numbers (first 5): {p1}, {p2}, {p3}, {p4}, {p5}")


if __name__ == "__main__":
    main()
