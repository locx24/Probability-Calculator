import copy
import random

class Hat:

  # pass in key-value pair dictionary into the constructor
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

  # draws a ball and removes the first occurrence of the color
    def draw(self, num_balls):
        num_balls = min(num_balls, len(self.contents))
        balls_drawn = random.sample(self.contents, num_balls)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls match the expected balls
        success = True
        for color, count in expected_balls.items():
            if balls_drawn.count(color) < count:
                success = False
                break

        if success:
            success_count += 1

    probability = success_count / num_experiments
    return probability
