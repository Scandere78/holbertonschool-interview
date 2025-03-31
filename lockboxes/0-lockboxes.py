#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes (list of list of int): A list of lists where each list contains integers that represent keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize the list to track unlocked boxes
    unlocked = [False] * len(boxes)
    
    # The first box is always unlocked
    unlocked[0] = True
    
    # Keep track of boxes to check
    keys = [0]  # We start by having access to box 0
    
    while keys:
        # Get the next box to check
        current_box = keys.pop()
        
        # Loop through the keys in the current box
        for key in boxes[current_box]:
            # If the key unlocks a box that hasn't been unlocked yet
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)  # Add this box to the list of boxes to check
    
    # If all boxes are unlocked, return True
    return all(unlocked)
