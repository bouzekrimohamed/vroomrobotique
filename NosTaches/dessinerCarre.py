import math
import time

class Robot:
    def __init__(self, x, y, orientation):
        self.x = x  # Position sur l'axe X
        self.y = y  # Position sur l'axe Y
        self.orientation = orientation  # Orientation en degrés (0 = vers le haut)
    
    def avancer(self, distance):
        # Convertir l'orientation en radians
        rad = math.radians(self.orientation)
        # Mettre à jour les positions x et y en fonction de la direction
        self.x += round(distance * math.cos(rad))
        self.y += round(distance * math.sin(rad))
        print(f"Avance à ({self.x}, {self.y})")
    
    def tourner(self, angle):
        # Mettre à jour l'orientation
        self.orientation = (self.orientation + angle) % 360
        print(f"Tourne à {self.orientation}°")
    
    def tracer_carre(self, cote):
        for _ in range(4):
            self.avancer(cote)  # Avancer d'un côté du carré
            self.tourner(90)  # Tourner à 90° à droite

# Simulation
if __name__ == "__main__":
    # Initialisation du robot à la position (0, 0) orienté vers le haut (0°)
    robot = Robot(x=0, y=0, orientation=0)
    
    print("Début de la simulation...")
    robot.tracer_carre(cote=10)  # Tracer un carré avec des côtés de 10 unités
    print("Simulation terminée.")
