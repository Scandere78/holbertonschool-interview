# Count it!

Projet Holberton : `count_it`

---

## Description

Ce projet consiste à écrire une fonction **récursive** en Python qui utilise l’API Reddit pour analyser les articles "hot" d’un subreddit donné.  
La fonction compte combien de fois une liste de mots-clés apparaît dans les titres de ces articles.

Le programme affiche ensuite les résultats triés :

- Par nombre d’occurrences (ordre décroissant).
- Puis par ordre alphabétique (croissant) en cas d’égalité.

Les mots sont traités de manière **insensible à la casse** (majuscule/minuscule) et affichés en **minuscules**.  
Les mots qui n’apparaissent pas ne sont pas affichés.

---

## Prototype

```python
def count_words(subreddit, word_list)

