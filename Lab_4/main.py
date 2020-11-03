def parse_input(filename):
    with open(filename, "r") as file:
        text = file.read()

        neighbours_dict = {}
        colors_dict = {}

        neighbours_list, colours = text.split('-')

        neighbours_list = neighbours_list.strip().replace(' ', '').replace('{', '').replace('}', '')
        for line in neighbours_list.split('\n'):
            node, neighbours = line.split(':')

            neighbours_dict[node] = neighbours.split(',')

        colours = colours.strip().replace(' ', '').replace('{', '').replace('}', '')

        for line in colours.split('\n'):
            node, color_list = line.split(':')
            colors_dict[node] = color_list.split(',')

        return neighbours_dict, colors_dict


def remove_inconsistent_values(xi, xj):
    removed = False
    for x in colors[xi]:
        cool = False
        for y in colors[xj]:
            if x != y:
                cool = True
        if not cool:
            colors[xi].remove(x)
            removed = True
    return removed


def ac3(csp: list):
    queue = csp.copy()
    while len(queue) > 0:
        (xi, xj) = queue.pop()
        if remove_inconsistent_values(xi, xj):
            for neighbor in neighbors[xi]:
                queue.append((neighbor, xi))


neighbors, colors = parse_input("input.txt")

print("Neighbors:")
print(neighbors)

constraints = []

for key in neighbors:
    for value in neighbors[key]:
        constraints.append((key, value))

print("Constraints:")
print(constraints)

print("Initial colors:")
print(colors)

ac3(constraints)

print("Colors after AC3:")
print(colors)
