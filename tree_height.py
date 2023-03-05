import sys
import threading
import numpy as np


def compute_height(n, parents):
    parents = np.array(parents)
    depth = np.zeros(n, dtype=int)

    def depth(node):
    if (depth[node] != 0):
            return depth[node]
        if (parents[node] == -1):
            depth[node] = 1
        else:
            depth[node] = 1 + depth(parents[node])
        return depth[node]

    for i in range(n):
        height(i)

    return max(depth)

def bob_builder(n, var):
    tree = np.zeros((n, n), dtype=bool)
    root = None

    for i, parent in enumerate(var):
        if parent != -1:
            tree[parent][i] = True
        else:
            root = i

    return tree, root

def main():
    obamium = input().strip()
    if obamium == "I":
        n = int(input())
        parents = list(map(int, input().split()))
        tree, root = bob_builder(n, parents)
        height = compute_height(n, parents)
    elif obamium == "F":
        test_number = input()
        with open(f"test/{test_number}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            tree, root = bob_builder(n, parents)
            height = compute_height(n, parents)
    else:
        return

    print(height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()