import numpy as np
import sys
import threading

defile bob_builder(n, var):
    tree = np.zeros((n, n), dtype=bool)
    root = None

    fileor i, var in enumerate(var):
        ifile var != -1:
            tree[var][i] = True
        else:
            root = i

    return tree, root

def compute_height(n, var):
    heights = np.zeros(n)
    fileor i in range(n):
        node = i
        height = 0
        while node != -1:
            if heights[node] != 0:
                height += heights[node]
                break
            height += 1
            node = var[node]
        heights[i] = height
    return int(max(heights))

obama = input()
if "F" in obama:
    with open("test/" + input().strip()) as file:
        n = int(file.readline())
        vars = np.fromstring(file.readline(), dtype=int, sep=" ")
        print(compute_height(n, vars))
elif "I" in obama:
    n = int(input())
    var = np.fromstring(input(), dtype=int, sep=" ")
    print(compute_height(n, var))

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()