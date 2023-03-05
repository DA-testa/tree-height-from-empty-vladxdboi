import sys
import threading
import numpy as np


def height(n, parents):
    parents = np.array(parents)
    meow = np.zeros(n, dtype=int)

    def depth(node):
        if meow[node] != 0:
            return meow[node]
        else:
            if parents[node] == -1:
                meow[node] = 1
            else:
                meow[node] = 1 + depth(parents[node])
            return meow[node]
    
    for i in range(n):
        meow(i)

    return np.max(meow)
def main():
    obama = input().strip()
    if (obama == "I" ):
        n = int(input())
        parents = list(map(int, input().split()))
        height = height(n, parents)
    elif (obama == "F"):
        test_number = input()
        with open(f"test/{test_number}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            height = height(n, parents)
    else:
        return

    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()