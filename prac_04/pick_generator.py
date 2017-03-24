import random

quick_picks = []

quick_pick_range = range(45)
quick_pick_length = 6
quick_pick_iterations = int(input("How many quick picks: "))

while quick_pick_iterations > 0:
    for i in range(quick_pick_length):
        random_number = random.randint(1, 45)
        quick_picks.append(random_number)
        if len(quick_picks) != len(set(quick_picks)):
            quick_picks = []
            for j in range(quick_pick_length):
                random_number = random.randint(1, 45)
                quick_picks.append(random_number)

    order = sorted(quick_picks)
    print(*order)
    quick_picks = []
    quick_pick_iterations -= 1
