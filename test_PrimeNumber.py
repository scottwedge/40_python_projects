#!/usr/bin/env python3

# tests for Prime Number App

# Imports
from PrimeNumber_While_Challenge_3 import *

# Functions

def test_check_if_prime_true():
    assert check_if_prime(11) == True

def test_check_if_prime_false():
    assert check_if_prime(100) == False

def test_calculate_primes(mocker):
    mocker.patch("PrimeNumber_While_Challenge_3.get_bounds", return_value = (11,21))
    assert calculate_primes() == [11,13,17,19]

