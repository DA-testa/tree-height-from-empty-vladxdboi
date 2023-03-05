import numpy as np
import sys
import threading

def bob_builder(n, var):
    tree = np.zeros((n, n), dtype=bool)
    root = None

    for i, var in enumerate(var):
        if var != -1:
            tree[var][i] = True
        else:
            root = i

    return tree, root

def compute_height(n, var):
    root = np.where(var == -1)[0][0]
    tree = [[] for _ in range(len(var))]
    for i, parent in enumerate(var):
        if parent != -1:
            tree[parent].append(i)

    def height(joop):
        children = tree[joop]
        if not children:
            return 1
        return 1 + np.max([height(child) for child in children])
    return height(root)

def main():
    inputz = input()
    if "F" in inputz:
        name = input().strip()
        with open("test/" + name) as file:
            n, *parents = map(int, file.readline().split())
            parents = np.array(parents)
            print(compute_height(n, parents))

    elif "I" in inputz:
        n, *parent = map(int, input().split())
        parent = np.array(parent)
        print(compute_height(n, parent))

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()