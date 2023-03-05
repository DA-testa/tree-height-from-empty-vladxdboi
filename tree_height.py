import sys
import threading
import numpy as np


def compute_height(n, parents):
    parents = np.array(parents)
    depth = np.zeros(n, dtype=int)

    def depthium(node):
        if depth[node] != 0:
            return depth[node]

        depth[node] = 1 + depthium(parents[node]) 
            if parents[node] != -1 
                else 1
        return depth[node]
    
    for i in range(n):
        depthium(i)

    return np.max(depth)
def main():
    obamium = input().strip()
    if (obamium == "I" ):
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
    elif (obamium == "F"):
        test_number = input()
        with open(f"test/{test_number}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            height = compute_height(n, parents)
    else:
        return

    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()