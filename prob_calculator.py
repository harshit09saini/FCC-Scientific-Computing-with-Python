import copy
import random


# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, balls_to_draw):
        balls_drawn = []
        for _ in range(balls_to_draw):

            total_balls = len(self.contents)

            if balls_to_draw >= total_balls:
                return self.contents

            rand_index = random.randint(0, total_balls - 1)
            ball_to_move = self.contents.pop(rand_index)
            balls_drawn.append(ball_to_move)

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_expected_outcomes = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if balls_drawn.count(key) < value:
                success = False
                break

        if success:
            num_expected_outcomes += 1

    probability = round(float(num_expected_outcomes) / float(num_experiments), 3)
    return probability
