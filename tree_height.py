import sys
import threading
import numpy as np

def build_tree(n, parents):
    tree = {}
    index = 0
    
    for i in range(n):
        tree[i] = []
    
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)
        else:
            index = i
            
    return tree, index

def compute_height(tree, index):
    tree = [(index, 1)]
    max = 0
    while tree:
        node, height = tree.pop(0)
        max = max(max, height)
        for child in tree[node]:
            tree.append((child, height+1))
            
    return max

def main():
    obama = input().strip()
    if (obama == "I" ):
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
    elif (obama == "F"):
        num = input()
        with open(f"test/{num}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            tree, index = build_tree(n, parents)
            height = compute_height(tree, index)
    else:
        return

    print(height)

    sys.setrecursionlimit(10**7) 
    threading.stack_size(2**27) 
    threading.Thread(target=main).start()