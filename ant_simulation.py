import numpy as np

# define a closed curve
def f(x,y):
    return  ( (x - 2.5) / 30 )**2 + ( (y - 2.5) / 40 )**2 - 1 


# simulate the process 1000 times
step_sum = 0
for i in range(100000):
    x,y,step = 0,0,0
    # while the ant (x,y) is inside the closed curve
    # the ant moves in 4 directions with the same probabilities
    # repeat the process until the ant go out of the curve
    while f(x,y) <0:
        direction = np.random.randint(low = 0, high =4)
        if direction == 0:
            x += 10
        if direction == 1:
            x -= 10
        if direction == 2:
            y += 10
        if direction == 3:
            y -= 10
        # count the number of total steps
        step += 1
    step_sum += step
    
step_sum/100000