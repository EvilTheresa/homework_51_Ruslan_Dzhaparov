from django.db import models
import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.satiety = 40
        self.happiness = 40
        self.asleep = False
        self.update_avatar()

    def feed(self):
        if not self.asleep:
            self.satiety = min(100, self.satiety + 15)
            self.happiness = min(100, self.happiness + 5)
            if self.satiety > 100:
                self.happiness = max(0, self.happiness - 30)
        self.update_avatar()

    def play(self):
        if self.asleep:
            self.asleep = False
            self.happiness = max(0, self.happiness - 5)
        else:
            self.satiety = max(0, self.satiety - 10)
            if random.randint(1, 3) == 1:
                self.happiness = 0
            else:
                self.happiness = min(100, self.happiness + 15)
        self.update_avatar()

    def sleep(self):
        self.asleep = True
        self.update_avatar()

    def update_avatar(self):
        if self.happiness < 30:
            self.avatar = 'img/sad_cat.jpg'
        elif self.happiness < 70:
            self.avatar = 'img/cat.jpg'
        else:
            self.avatar = 'img/happy_cat.jpg'
