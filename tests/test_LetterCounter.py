#!/usr/bin/env python3

import LetterCounter_Project_1 as LC


# Tests
def test_pass():
    assert True

def test_count_letters():
    assert LC.count_letters("hello there", "h") == 2

def test_cap_user_name():
    assert LC.cap_user_name("mike") == "Mike"
