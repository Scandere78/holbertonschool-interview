#!/usr/bin/python3

def canUnlockAll(boxes):
    # Crée une liste pour savoir si les boîtes sont déverrouillées
    unlocked = [False] * len(boxes)
    
    # La première boîte est toujours déverrouillée
    unlocked[0] = True
    
    # Liste des boîtes à vérifier, on commence avec la boîte 0
    keys = [0]
    
    while keys:
        # On prend une boîte à vérifier
        current_box = keys.pop()
        
        # On vérifie les clés dans cette boîte
        for key in boxes[current_box]:
            # Si la clé permet d'ouvrir une boîte non déverrouillée
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)  # Ajouter cette boîte à vérifier
    
    # Si toutes les boîtes sont déverrouillées, on retourne True
    return all(unlocked)
