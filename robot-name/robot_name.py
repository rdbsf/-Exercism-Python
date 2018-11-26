import string
import random

class Robot:
    robots = []
    def __init__(self):
        self.makeName()

    def makeName(self):
        while(1):
            name = random.choice(string.ascii_letters).upper() + random.choice(string.ascii_letters).upper() + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
            if (name not in self.robots):
                self.name = name
                self.robots.append(name)
                break

    def reset(self):
        self.makeName()
