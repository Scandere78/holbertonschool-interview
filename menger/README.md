# 🧩 2D Menger Sponge in C

This project implements a 2D version of the Menger Sponge using the C programming language. It visually prints a fractal pattern of `#` and space characters in the terminal according to a given recursion level.

---

## 📐 What is a Menger Sponge?

A Menger Sponge is a 3D fractal curve, but here we focus on its **2D projection**. The construction follows a recursive pattern:

- **Level 0**: A single `#` character.
- **Level N**: A `3^N × 3^N` grid where each cell contains a smaller sponge of level `N-1`, except the center of every 3x3 block, which is empty.


---

## 🔧 Compilation

Use `gcc` with math library:

```bash
gcc -Wall -Wextra -Werror -pedantic -o 0-menger 0-menger.c 0-main.c -lm



