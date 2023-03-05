import sys
import threading
import numpy as np

def bob_builder(n, var):
    tree = {i: [] for i in range(n)}
    root = -1
    for i, parent in enumerate(var):
        if parent != -1:
            tree[parent].append(i)
        else:
            root = i
    return tree, root

def compute_height(tree, index):
    queue = [(index, 1)]
    max = 0
    while queue:
        node, height = queue.pop(0)
        max = max(max, height)
        queue.extend((child, height+1) for child in tree[node])
    return max

def main():
    input = input().strip()
    if input == "F":
        file_name = input().strip()
        if "a" in file_name:
            return
        with open(f"./test/{file_name}", mode="r") as file:
            n, *var = map(int, file.read().split())
            var = np.array(var)
    elif input == "I":
        n, *var = map(int, input().split())
        var = np.array(var)
    else:
        return

    tree, index = bob_builder(n, var)
    print(compute_height(tree, index))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
