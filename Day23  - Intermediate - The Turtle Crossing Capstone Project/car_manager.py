from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    
    def __init__(self):
        self.cars = [] 
        self.generate_car()
        

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.goto(280, random.randint(a=-220, b=250))
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            new_car.shape("square")
            new_car.setheading(180)
            new_car.turtlesize(stretch_len=2)

            self.cars.append(new_car)
    
    def move_forward(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
    
    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player.position()) < 30:
                return False
        
        return True
    



    
    