"""
can_unlock_all function as a solution.
"""

def isLonger(routes, maxlen):
    """
    checks if any of the possible routes is longer than maxlen.
    """
    lens = [len(route) for route in routes] or [0]
    return max(lens) >= maxlen


def isPossible(routes, length):
    """
    checks the the different solutions routes
    to determine if it's possible to open the boxes.
    """
    sol = set(range(length))
    potentials = [set(potential_sol) for potential_sol in routes if len(potential_sol) >= length]
    for potential in potentials:
        if potential == sol:
            return True
    return False


def canUnlockAll(boxes):
    """
    solution to the boxes problem.
    """
    num_boxes = len(boxes)
    routes = []
    for initial in boxes[0]:
        routes.append([0, initial])

    while not isLonger(routes, int(num_boxes * 1.5)) and routes:
        candidate_route = routes.pop(0)
        next_box = boxes[candidate_route[-1]]
        for new_path in next_box:
            new_route = candidate_route + [new_path]
            routes.append(new_route)

        if not routes:
            routes.append(candidate_route)
            break

    return isPossible(routes, num_boxes)
