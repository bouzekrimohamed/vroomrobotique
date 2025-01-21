import math

class Robot:
    def __init__(self, x, y, orientation, distance_entre_roues):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.vitesse_gauche = 0
        self.vitesse_droite = 0
        self.distance_entre_roues = distance_entre_roues

    def avancer(self, duree, vg, vd):
        self.vitesse_gauche = vg
        self.vitesse_droite = vd

        vitesse_moyenne = (self.vitesse_gauche + self.vitesse_droite) / 2
        omega = (self.vitesse_droite - self.vitesse_gauche) / self.distance_entre_roues
        self.orientation = (self.orientation + math.degrees(omega) * duree) % 360
        
        distance = vitesse_moyenne * duree
        rad = math.radians(self.orientation)
        self.x += distance * math.cos(rad)
        self.y += distance * math.sin(rad)

        print(f"Position: ({self.x:.2f}, {self.y:.2f}), Orientation: {self.orientation:.2f}°")

    def tourner_90_degres(self, vg, vd):
        omega = (vd - vg) / self.distance_entre_roues
        temps_rotation = (math.pi / 2) / omega
        self.avancer(temps_rotation, vg, vd)

class Simulation:
    def __init__(self, robot):
        self.robot = robot

    def lancer(self):
        print("Début de la simulation...")

        self.robot.avancer(1, 5, 5)
        self.robot.tourner_90_degres(5, 10)

        print(f"Position finale: ({self.robot.x:.2f}, {self.robot.y:.2f}), Orientation: {self.robot.orientation:.2f}°")
        print("Simulation terminée.")

robot = Robot(x=0, y=0, orientation=0, distance_entre_roues=2)
simulation = Simulation(robot)

simulation.lancer()
