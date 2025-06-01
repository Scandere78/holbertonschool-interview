#!/usr/bin/python3
"""
Module 0-validate_utf8
This module defines the function validUTF8 which checks if a list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validates if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing byte values.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        if byte < 0 or byte > 255:  # Vérification des valeurs invalides
            return False

        if num_bytes == 0:
            if byte & 0b10000000 == 0:  # 1-byte character (ASCII)
                continue
            elif byte & 0b11100000 == 0b11000000:  # 2-byte character
                num_bytes = 1
            elif byte & 0b11110000 == 0b11100000:  # 3-byte character
                num_bytes = 2
            elif byte & 0b11111000 == 0b11110000:  # 4-byte character
                num_bytes = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            num_bytes -= 1

    return num_bytes == 0
