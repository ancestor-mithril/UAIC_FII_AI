import algorithms as alg
import ai_operations as ai
import numpy as np

maze = ai.get_problem_instance(10, 10)
fd = open("input.txt", "r")
xs, ys, xd, yd = map(int, fd.read().split())

maze = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

print("Initial maze:")
print(maze)
print("Starting position: (" + str(xs) + ", " + str(ys) + ")")
print("Ending position: (" + str(xd) + ", " + str(yd) + ")")

for algorithm in [alg.solve_bkt, alg.solve_lee]:
    print("\nTrying " + str(algorithm) + " algorithm...\n")
    solution_found, final_maze = algorithm(maze, xs, ys, xd, yd)

    print("Solution found: " + str(solution_found))
    if solution_found:
        print("Final maze:")
        print(final_maze)

algorithm = alg.solve_hill_climbing
print("\nTrying " + str(algorithm) + " algorithm...\n")
for i in range(1000):
    solution_found, final_maze = algorithm(maze, xs, ys, xd, yd)
    if solution_found:
        print("Solution found: " + str(solution_found))
        print("Final maze:")
        print(final_maze)
        break
else:
    print("Solution found: " + str(False))
