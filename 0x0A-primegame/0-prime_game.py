#!/usr/bin/python3
"""
Module solving the Prime Game challenge.
"""


def isPrime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    """
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if n < 1:
            continue
        current_set = set(range(1, n + 1))
        turn = 0
        while True:
            round_primes = [num for num in current_set if isPrime(num)]
            if not round_primes:
                ben_wins += 1 if turn == 0 else 0
                maria_wins += 1 if turn == 1 else 0
                break
            prime = min(round_primes)
            current_set = {num for num in current_set
                           if num % prime != 0}
            turn = 1 - turn
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None
