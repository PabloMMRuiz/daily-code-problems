
import random


def calc_pi(iterations=10000):
    points_in = 0

    current_pi = 0
    for n in range(1, iterations):
        x = random.random()
        y = random.random()

        if x**2 + y**2 < 1.0:
            points_in += 1
    current_pi =  points_in * 4.0 / iterations
    return current_pi

if __name__ == "__main__":
    print(calc_pi(100000000))