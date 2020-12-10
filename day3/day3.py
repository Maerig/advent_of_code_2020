from functools import reduce


SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


with open("input.txt") as f:
    trees = [l.strip() for l in f]


width = len(trees[0])
height = len(trees)


def get_tree(i, j):
    return trees[j][i % width]


def count_trees(slope):
    u, v = slope
    return sum(
        get_tree(i * u, i * v) == "#"
        for i in range(height // v)
    )


print(count_trees((3, 1)))
print(reduce(lambda x, y: x * y, (count_trees(slope) for slope in SLOPES)))
