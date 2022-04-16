from turtle import Turtle
from random import randint, choice

SPEED_INCREMENT = 5
Y = [x for x in range(-200, 200, 40)]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

        self.speed = 5
        self.generate_car()
        self.hideturtle()

    def generate_car(self):
        random_num = randint(1, 5)
        if random_num == 1:
            new_car = Turtle()        
            new_car.shape("square")
            new_car.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, choice(Y))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_left(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def add_speed(self):
        self.speed += SPEED_INCREMENT
