#!/usr/bin/python3
"Prime Game"


def sieve_of_eratosthenes(limit):
    """
    Generate all prime numbers up to the given limit using the Sieve of
    Eratosthenes algorithm.
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]


def play_game(n):
    """
    Simulate a game for a given value of n, where Maria and Ben take turns
    removing primes and their multiples from the set of integers from 1 to n.
    """
    primes = sieve_of_eratosthenes(n)
    numbers = [True] * (n + 1)
    turn = 0
    for prime in primes:
        if numbers[prime]:
            for i in range(prime, n + 1, prime):
                numbers[i] = False
            turn = 1 - turn
    return "Maria" if turn == 1 else "Ben"


def isWinner(x, nums):
    """
    Simulate multiple rounds of the game and determine who won the most
    rounds. The player with the most wins is returned. If there is a tie,
    return None.
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
