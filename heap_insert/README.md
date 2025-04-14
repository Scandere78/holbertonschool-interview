# Heap Insert

## 🇫🇷 Description du projet

Ce projet a pour objectif de manipuler une **Max Binary Heap** (tas binaire maximum). Une heap est une structure d’arbre binaire complète où chaque nœud parent a une valeur supérieure ou égale à ses enfants. Tu apprendras ici à :

- Créer des nœuds d’arbres binaires
- Insérer des valeurs dans une Max Heap
- Maintenir la propriété de Max Heap (Max Heap Order)

Les fichiers sont codés en C et suivent la norme **Betty**. Aucune variable globale n’est utilisée, et chaque fichier contient au maximum 5 fonctions.

### 📁 Fichiers importants

- `0-binary_tree_node.c` : création d’un nouveau nœud d’arbre binaire
- `1-heap_insert.c` : insertion d’une valeur dans un Max Binary Heap
- `binary_trees.h` : fichier d’en-tête contenant la structure et les prototypes
- `binary_tree_print.c` : utilisé uniquement pour visualiser l’arbre (non obligatoire dans le repo)

### 🔧 Compilation

```bash
gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 1-main.c 1-heap_insert.c 0-binary_tree_node.c -o heap_insert

