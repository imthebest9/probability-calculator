import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def __repr__(self):
        pass

    def draw(self, num):
        contents = self.contents
        if num >= len(contents):
            return contents

        drew = []

        for _ in range(num):
            len_contents = len(contents)
            index = random.randrange(len_contents)
            ball = contents[index]
            drew.append(ball)
            contents = contents[0:index] + contents[index + 1:]

        self.contents = contents

        return drew

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for n in range(num_experiments):
        hat_copy = copy.copy(hat)
        drew = hat_copy.draw(num_balls_drawn)
        success = True
        for key in expected_balls.keys():
            if drew.count(key) < expected_balls[key]:
                success = False
                break
        if success:
            m += 1

    return (m/num_experiments)
