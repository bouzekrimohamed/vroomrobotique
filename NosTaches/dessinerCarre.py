import math
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, x, y, orientation):
        self.x = x  
        self.y = y  
        self.orientation = orientation  
        self.vitesse_gauche = 0  
        self.vitesse_droite = 0  

    def avancer(self, duree, vg, vd):
        self.vitesse_gauche = vg
        self.vitesse_droite = vd

        vitesse_moyenne = (self.vitesse_gauche + self.vitesse_droite) / 2
        
        omega = (self.vitesse_droite - self.vitesse_gauche)  
        self.orientation = (self.orientation + math.degrees(omega) * duree) % 360
        
        distance = vitesse_moyenne * duree
        
        rad = math.radians(self.orientation)
        self.x += distance * math.cos(rad)
        self.y += distance * math.sin(rad)

        print(f"Position: ({self.x:.2f}, {self.y:.2f}), Orientation: {self.orientation:.2f}°")

    def tourner_90_degres(self, vg, vd):
       self.avancer(1, -vg, vd)  

class Simulation:
    def __init__(self, robot):
        self.robot = robot

    def lancer(self):
        print("Début de la simulation...")

        # Tracé du carré
        positions = [(self.robot.x, self.robot.y)] 
        self.robot.avancer(1, 5, 5)  
        positions.append((self.robot.x, self.robot.y))  

     
        self.robot.tourner_90_degres(5, 5) 
        positions.append((self.robot.x, self.robot.y)) 

        print(f"Position finale: ({self.robot.x:.2f}, {self.robot.y:.2f}), Orientation: {self.robot.orientation:.2f}°")
        print("Simulation terminée.")

        self.tracer(positions)

    def tracer(self, positions):
        plt.figure(figsize=(6, 6))

        x_vals, y_vals = zip(*positions)

        plt.plot(x_vals, y_vals, marker='o', color='blue', label='Trajectoire du robot')

        plt.plot([x_vals[0], x_vals[0] + 10], [y_vals[0], y_vals[0]], 'r--')  
        plt.plot([x_vals[0] + 10, x_vals[0] + 10], [y_vals[0], y_vals[0] + 10], 'r--') 
        plt.plot([x_vals[0] + 10, x_vals[0]], [y_vals[0] + 10, y_vals[0] + 10], 'r--') 
        plt.plot([x_vals[0], x_vals[0]], [y_vals[0] + 10, y_vals[0]], 'r--')  

        plt.xlim(0, 15)
        plt.ylim(0, 15)
        plt.xlabel('Position X')
        plt.ylabel('Position Y')
        plt.title('Simulation du robot et son mouvement')

        plt.legend()
        plt.grid(True)
        plt.show()

robot = Robot(x=0, y=0, orientation=0)
simulation = Simulation(robot)

simulation.lancer()
