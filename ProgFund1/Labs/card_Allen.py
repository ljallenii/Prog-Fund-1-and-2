import random

class Card:
    def __init__(self):
        self.__value = 0
        
    def deal(self):
        self.__value = random.randint(1,13)
        
    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def get_face_value(self):
        face_values = ["Joker", "Ace", "Two", "Three", "Four", "Five", "Six",
                       "Seven", "Eight", "Nine", "Ten", "Jack","Queen", "King"]
        return face_values[self.__value]

    def __str__(self):
        return "value: " + str(self.__value)
        
