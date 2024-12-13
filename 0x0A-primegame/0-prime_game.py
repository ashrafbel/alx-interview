#!/usr/bin/python3
"Prime Game"


def is_prime(n):
    """Determine if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_round(n):
    """
    Play a single round of the prime game.
    """
    primes = [p for p in range(2, n + 1) if is_prime(p)]
    if not primes:
        return 'Ben'
    removed = set()
    maria_turn = True
    while primes:
        current_prime = None
        for p in primes:
            if p not in removed:
                current_prime = p
                break
        if current_prime is None:
            return 'Ben' if maria_turn else 'Maria'
        removed.add(current_prime)
        for multiple in range(current_prime, n + 1, current_prime):
            removed.add(multiple)
        primes = [p for p in primes if p not in removed]
        maria_turn = not maria_turn
    return 'Ben' if maria_turn else 'Maria'


def isWinner(x, nums):
    """
    Determine the overall winner of multiple rounds.
    """
    if not nums or x == 0:
        return None
    maria_wins = 0
    ben_wins = 0
    for n in nums[:x]:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None