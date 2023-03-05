import numpy as np
import sys
import threading

def bob_builder(n, var):
    tree = np.zeros((n, n), dtype=bool)
    root = None
    for i, parent in enumerate(var):
        if parent != -1:
            tree[parent][i] = True
        else:
            root = i
    return tree, root

def compute_height(tree, root):
    queue = [(root, 1)]
    max = 0
    while queue:
        node, height = queue.pop(0)
        max = np.max([max, height])
        children = np.where(tree[node] == True)[0]
        queue.extend([(child, height + 1) for child in children])
    return max


def main():
    input = input().strip()
    if input == "I":
        n, *var = map(int, input().strip().split())
        var = np.array(var)
    else:
        return
    if input == "F":
        file = input().strip()
        if file == "a":
            return
        with open(f"./test/{file}", mode="r") as obama:
            n, *var = map(int, obama.read().split())
            var = np.array(var)

    tree, root = bob_builder(n, var)
    print(compute_height(tree, root))

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()