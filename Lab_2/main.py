import numpy as np
import maze_creator as f
import algorithms as alg
import ai_operations as ai


maze = ai.get_problem_instance(10, 10)
fd = open("input.txt", "r")
xs, ys, xd, yd = map(int, fd.read().split())

print(maze, 'maze\n', xs, ys, "xs, ys\n", xd, yd, "xd, yd\n")


# print(ai.get_initial_state(maze, xs, ys), '\n')
is_final = ai.is_final(maze, xd, yd)
is_valid = ai.is_transition_valid(maze, 2, 1)
# print("Is_Final:", is_final)
# print('Is_Valid:', is_valid)

print(alg.solve_bkt(maze, xs, ys, xd, yd))
# print(maze)
# print(alg.solve_lee(maze, xs, ys, xd, yd))

