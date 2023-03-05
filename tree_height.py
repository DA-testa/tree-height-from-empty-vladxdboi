import sys
import threading
import numpy as np


def height(n, parents):
    depth = [0] * n

    def depthium(node):
        if depth[node] != 0:
            return depth[node]
        depth[node] = 1 + depthium(parents[node]) if parents[node] != -1 else 1
        return depth[node]
    
    for i in range(n):
        depthium(i)

    return max(depth)

def main():
    obamium = input().strip()
    if obamium == "I":
        n, *parents = map(int, input().split())
    elif obamium == "F":
        test_number = input()
        with open(f"test/{test_number}", "r") as file:
            n, *parents = map(int, file.readline().strip().split())
    else:
        return

    height = height(n, parents)
    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()