# use python3

import sys
import threading
import queue
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Tree:
    def __init__(self, index, depth=None):
        self.val = index
        self.child = []
        self.depth = depth

    def add_child(self, child):
        self.child.append(child)

def cal_height(tree):
    node = None
    for x in tree:
        if x.depth == 0:
            # Breadth-first travel
            root = x
    fifo_queue = queue.Queue()
    fifo_queue.put(root)
    while not fifo_queue.empty():
        node = fifo_queue.get()
        if not node.child == []:
            for i in node.child:
                i.depth = node.depth + 1
                fifo_queue.put(i)
    print(node.depth + 1)


def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    node = n * [0]

    # CREAT TREE
    for index, dad in enumerate(parent):
        if node[index] == 0 and dad != -1:
            node[index] = Tree(index)
        if dad == -1:
            node[index] = Tree(index, depth=0)
            continue
        if node[dad] == 0:
            node[dad] = Tree(dad)
        node[dad].add_child(node[index])
    # CREATE TREE
    cal_height(node)


threading.Thread(target=main).start()
