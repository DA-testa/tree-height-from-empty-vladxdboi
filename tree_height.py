# 221RDB453 Vladislavs Senevičs, 11.grupa
import sys
import threading

def cheight(n, parents):
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
        n = int(input())
        parents = list(map(int, input().split()))
    elif obamium == "F":
        num = input()
        with open(f"test/{num}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
    else:
        return

    height = cheight(n, parents)
    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()