from fileinput import close
from queue import PriorityQueue
import heapq
from scramble_cube import *
import numpy as np


class Nesto:

    def __lt__(self, other):
        # p1 < p2 calls p1.__lt__(p2)
        return self.dicter['cost'] < other.dicter['cost']

    def __eq__(self, other):
        # p1 == p2 calls p1.__eq__(p2)
        return self.dicter['cost'] == other.dicter['cost']

    def __init__(self, dict) -> None:
        self.dicter = dict


def all_star(start_state, model):
    open_list = []
    #closed_list = []

    state_dict = {
        'parent': None,
        'action': None,
        'cube_state': start_state,
        'cost': 0
    }

    visited = set()

    heapq.heappush(open_list, (0, Nesto(state_dict)))
    while (len(open_list) != 0):
        key, djura = heapq.heappop(open_list)
        state = djura.dicter
        if check_if_final(state['cube_state']):
            actions = []
            parent = state

            while parent['parent'] is not None:
                actions.insert(0, parent['action'])
                parent = parent['parent']

            return actions

        for m in moves:
            if state['action'] is not None and m == get_oposite(state['action']):
                continue

            new_cube_state = get_state_copy(state['cube_state'])
            rotate_cube(new_cube_state, m, moves.index(m[0]))

            if (tuple(new_cube_state) in visited):
                continue

            new_state = {
                'parent': state,
                'action': m,
                'cube_state': new_cube_state,
                'cost': float(model(np.expand_dims(new_cube_state, axis=0)))
            }
            keyic = new_state['cost']
            heapq.heappush(open_list, (keyic, Nesto(new_state)))

        visited.add(tuple(state['cube_state']))

        # if state not in closed_list:
        #     closed_list.append(state)

    return []
