# Exercice 6 — Garden Analytics

## À faire

- [ ] Créer `ex6/ft_garden_analytics.py` à partir de l’exercice 5.

### Méthodes spéciales de Plant

- [x] Ajouter une méthode statique (`@staticmethod`) qui indique si un âge dépasse un an.
- [ ] Tester avec 30 jours (`False`), 365 jours (`False`) et 400 jours (`True`).
- [ ] Ajouter une méthode de classe (`@classmethod`) pour créer une plante anonyme avec des valeurs par défaut.

### Classe Seed

- [ ] Créer `Seed`, qui hérite de `Flower`.
- [ ] Ajouter un attribut pour le nombre de graines, initialisé à zéro.
- [ ] Mettre à jour le nombre de graines après la floraison.
- [ ] Adapter `show()` pour afficher aussi le nombre de graines.

### Statistiques

- [ ] Créer une classe interne à `Plant` pour stocker les statistiques.
- [ ] Donner à chaque plante son propre objet de statistiques.
- [ ] Protéger les attributs des statistiques avec la convention `_`.
- [ ] Compter les appels à `grow()`, `age()` et `show()`.
- [ ] Prévoir une méthode d’affichage des statistiques.
- [ ] Éviter de compter deux fois un appel lors de l’utilisation de `super()`.
- [ ] Ajouter aux arbres un compteur des appels à `produce_shade()`.
- [ ] Créer une fonction hors des classes pour afficher les statistiques de n’importe quel type de plante.

### Démonstration et vérifications

- [ ] Compléter `main()` pour démontrer les nouvelles fonctionnalités.
- [ ] Vérifier que les compteurs évoluent correctement.
- [ ] Vérifier que les statistiques des différentes plantes sont indépendantes.
- [ ] Vérifier que le programme s’exécute sans erreur.
- [ ] Vérifier les annotations de type avec mypy.
- [ ] Vérifier le style avec flake8.

## Fonctions autorisées

`super()`, `print()`, `range()`, `round()`, `staticmethod()`, `classmethod()`.

## Fichier à rendre

`ex6/ft_garden_analytics.py`
