#!/usr/bin/python3
"Prime Game"


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_round(n):
    """
    Simulate a single round of the prime game.
    """
    numbers = set(range(1, n + 1))
    maria_turn = True
    while True:
        available_primes = [num for num in numbers if is_prime(num)]
        if not available_primes:
            return 'Ben' if maria_turn else 'Maria'
        prime = min(available_primes)
        numbers = {num for num in numbers if num % prime != 0}
        maria_turn = not maria_turn


def isWinner(x, nums):
    """Determine the overall winner of multiple game rounds."""
    if not nums or x == 0:
        return None
    maria_wins = 0
    ben_wins = 0
    for n in nums:
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
