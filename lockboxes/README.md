Lockboxes
Overview
This project involves a challenge where you have a number of locked boxes in front of you. Each box may contain keys to other boxes, and the goal is to determine whether all the boxes can be unlocked.

The boxes are numbered sequentially from 0 to n-1, and a key in a box can unlock another box. The first box (box 0) is always unlocked.

The task is to write a method to check if all the boxes can be opened.

Requirements
General:

Allowed editors: vi, vim, emacs

Files should be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3)

All files must end with a new line.

The first line of every Python file should be #!/usr/bin/python3

A README.md file is mandatory at the root of the project.

The code must be documented and adhere to PEP 8 (version 1.7.x).

All files must be executable.

Tasks
0. Lockboxes (Mandatory)
You are given n locked boxes numbered from 0 to n-1. Each box may contain keys to other boxes. Your task is to write a function canUnlockAll to determine if all boxes can be opened.

Prototype:

python
Copier
Modifier
def canUnlockAll(boxes):
Input:

boxes is a list of lists. Each inner list represents a box and contains keys that can unlock other boxes.

The first box boxes[0] is always unlocked.

Output:

Return True if all the boxes can be opened, otherwise return False.

Constraints:

All keys are positive integers.

There may be keys that do not open any box.

You can assume that there will always be keys available in the first box.

Example:
python
Copier
Modifier
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
Requirements:
Implement the function canUnlockAll(boxes) in the file 0-lockboxes.py.

File Descriptions:
main_0.py: This file demonstrates the usage of the canUnlockAll function. It tests multiple sets of boxes to check if all boxes can be unlocked.

0-lockboxes.py: Contains the implementation of the canUnlockAll function.

Example usage:
bash
Copier
Modifier
$ python3 main_0.py
True
True
False
Installation
To run the project, make sure you have Python 3 installed on your machine. You can clone the repository and run the main_0.py file directly:

bash
Copier
Modifier
$ git clone https://github.com/yourusername/lockboxes.git
$ cd lockboxes
$ python3 main_0.py
Documentation
The project uses Python 3, and the function canUnlockAll is implemented in 0-lockboxes.py. It takes in a list of boxes and checks if all boxes can be unlocked by simulating the opening process with the available keys.

Contributing
Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

License
This project is open-source and available under the MIT License.