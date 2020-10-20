import algorithms as alg
import ai_operations as ai
import numpy as np

maze = ai.get_problem_instance(15, 15)
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
# labirint fara bazine de acumulare in minime locale extinse pe toata suprafata de cautare a algoritmului hillclimbing


print("Initial maze:")
print(maze)
print("Starting position: (" + str(xs) + ", " + str(ys) + ")")
print("Ending position: (" + str(xd) + ", " + str(yd) + ")")

<<<<<<< HEAD
for algorithm in [alg.solve_bkt, alg.solve_lee, alg.solve_hill_climbing]:
    print("\nTrying " + str(algorithm).split()[1] + " algorithm...\n")
=======
for algorithm in [alg.solve_bkt, alg.solve_lee, alg.solve_hill_climbing, alg.solve_simulated_annealing]:
    print("\nTrying " + str(algorithm) + " algorithm...\n")
>>>>>>> 19d34d5325b431cf61bfd760c2c71f0380d202a9
    solution_found, final_maze = algorithm(maze, xs, ys, xd, yd)

    print("Solution found: " + str(solution_found))
    if solution_found:
        print("Final maze:")
        print(final_maze)

# algorithm = alg.solve_hill_climbing
# print("\nTrying " + str(algorithm) + " algorithm...\n")
# for i in range(1000):
#     solution_found, final_maze = algorithm(maze, xs, ys, xd, yd)
#     if solution_found:
#         print("Solution found: " + str(solution_found))
#         print("Final maze:")
#         print(final_maze)
#         break
# else:
#     print("Solution found: " + str(False))
