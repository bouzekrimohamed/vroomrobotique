<u>**1-Méthode de rotation par vitesses différentielles**</u>


    Principe :
        Si les deux roues tournent à des vitesses identiques, le robot avance en ligne droite.
        Si une roue tourne plus vite que l’autre, le robot décrit une courbe ou effectue une rotation.
        Pour une rotation sur place, une roue tourne dans le sens horaire et l’autre dans le sens antihoraire.

Exemple de vitesses :

    Ligne droite : Vitesse gauche = 10, Vitesse droite = 10.
    Rotation vers la gauche : Vitesse gauche = -5, Vitesse droite = 5.
    Courbe douce vers la droite : Vitesse gauche = 10, Vitesse droite = 5.

<u>**2. Tâches à réaliser :**</u>

    Tracer un carré :
        Avancer en ligne droite pendant une certaine distance.
        Tourner de 90° en ajustant les vitesses des roues.
        Répéter cette séquence 4 fois pour compléter le carré.

    S’approcher d’un mur :
        Utiliser le capteur de distance pour détecter le mur.
        Réduire progressivement la vitesse à mesure que la distance au mur diminue.

    Suivre une balise :
        Utiliser la caméra pour repérer la balise (par exemple, une couleur ou une forme spécifique).
        Ajuster la direction en fonction de la position relative de la balise dans le champ de vision.

<u>**3. Simulation dans la console :**</u>

La simulation représentera :

    Le robot comme un point (x, y) sur une grille 2D.
    Les roues comme deux points distincts permettant de calculer les mouvements différenciés.
    La caméra comme un élément essentiel pour des tâches complexes.

Les capteurs seront simulés :

    Capteur de distance : Retourne une distance au mur selon la direction actuelle.
    Caméra : Simule la détection d’une balise en donnant une position relative sur la grille.

<u>**4. Étapes pour coder la simulation :**</u>

    Représentation des éléments :
        Un point pour le robot et deux points pour les roues.
        Une grille 2D pour simuler l’environnement.

    Rotation par vitesses différentielles :
        Calculer l’angle de rotation basé sur la différence de vitesses entre les roues.
        Mettre à jour la position (x, y) du robot et son orientation.

    Simuler les capteurs :
        Capteur de distance : Retourne une valeur calculée en fonction de la position et de la direction du robot.
        Caméra : Simule la détection d’une balise.

    Tâches simulées :
        Implémenter les trois tâches définies (tracer un carré, approcher un mur, suivre une balise).
![9d7e52b5-2304-45c6-ac8d-dec30da333b8](https://github.com/user-attachments/assets/5204d00b-a0d0-4249-b7be-1ff512c06926)

