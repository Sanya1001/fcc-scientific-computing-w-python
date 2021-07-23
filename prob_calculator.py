import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    draw_balls = []
    for i in range(number):
      random_ball = random.randrange(len(self.contents), step=1)
      draw_balls.append(self.contents.pop(random_ball))
    return draw_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  match = 0
  exp_balls_content = []

  for key in expected_balls:
      exp_balls_content.append(expected_balls[key])
  
  for _ in range(num_experiments):
    hatx = copy.deepcopy(hat)
    drawn_balls = hatx.draw(num_balls_drawn)

    drawn_balls_content = []
    for key in expected_balls:
      drawn_balls_content.append(drawn_balls.count(key))

    if drawn_balls_content >= exp_balls_content:
      match += 1

  return match/ num_experiments
