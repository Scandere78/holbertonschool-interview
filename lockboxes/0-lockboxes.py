#!/usr/bin/python3
"""
Module 0-lockboxes
This module defines the function canUnlockAll which checks
if all the boxes in a list of lists can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists where each list
        contains integers that represent keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = [False] * len(boxes)  # Initialize unlocked boxes
    unlocked[0] = True  # First box is always unlocked
    keys = [0]  # Start with access to box 0

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)  # Add this box to check

    return all(unlocked)
