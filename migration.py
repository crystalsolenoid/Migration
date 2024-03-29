import os
import random as rnd
import time

BIRD = "⋎"

# Other birds to try someday:
"⏠ ⏠"
"⁔⁔"
"⁀⁀"
"⏟"

DELAY = 0.1

def clamp(low, val, high):
    return sorted((low, val, high))[1]

def nth_birds(n, pos, line):
    bounds = range(0, len(line))
    left = pos - n
    right = pos + n
    if left in bounds:
        line[left] = BIRD
    if right in bounds:
        line[right] = BIRD

def new_flock(width):
    position = rnd.randrange(width)
    length = 0
    max_length = int(rnd.gauss(4, 1))
    return [position, length, max_length]

def main():
    width = os.get_terminal_size()[0]

    # flock data structure:
    # [position, current length, max length]
    flocks = [[width // 2, 0, 7]]

    while True:
        width = os.get_terminal_size()[0]
        line = [" "] * width
        for flock in flocks:
            if flock[1] <= flock[2]:
                nth_birds(flock[1], flock[0], line)
                flock[1] += 1
        print("".join(line))

        # cull finished flocks
        flocks = [f for f in flocks if f[1] <= f[2]]

        if rnd.randrange(6) == 0:
            flocks.append(new_flock(width))
        time.sleep(DELAY)

try:
    main()
except KeyboardInterrupt:
    print("\nMigration, by Quinten Konyn quintenkonyn.recurse.com")
