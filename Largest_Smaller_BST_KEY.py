"""
Largest Smaller BST Key
Given a root of a Binary Search Tree (BST) 
and a number num, implement an efficient 
function findLargestSmallerKey that finds 
the largest key in the tree that is smaller than num. 
If such a number doesn’t exist, return -1. 
Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.

"""

# HINTS

"""
Largest Smaller BST Key
First, make sure your peer understands the question.
If you or your peer have a hard time understanding 
how to go about solving this problem, or could use 
a reminder of how BSTs work, take this interactive BST application for a spin.
Some tend to first look for num in the tree and then look for its predecessor.
However, num isn’t necessarily a key in the given tree. It could be any number. 
Moreover, even if num is in the tree, finding it first won’t help.
To get the full score for problem solving, 
your peer must be able to explain why it’s possible to always store the 
last key smaller than num without comparing it to the previously stored key.

"""

# ANSWER

"""
Largest Smaller BST Key
While the code to solve this question is pretty simple, it takes some understanding of binary search trees. There are two key parts for the algorithm.

Part 1: traversing the tree

A node in a binary search tree is larger than all keys in its left subtree 
and smaller than all keys i its right subtree. Starting from the root, for each node we choose 
its left or its right child as the next step, 
based on a comparison between that node’s key and num: 
If the current node holds a key smaller than num, we proceed 
to its right subtree looking for larger keys. Otherwise, 
we proceed to its left subtree looking for smaller keys.

Part 2: finding the key

During this iteration, when the current key is smaller than num, 
we store it as our result and keep looking for a larger key that is still smaller than num.

It’s important to understand why we always store the last key 
without comparing it to the value stored beforehand. If we have stored a key before, 
then it means we have chosen to continue down the key’s right subtree. 
Therefore, all subsequent keys will be larger than any previously stored keys.

"""

function findLargestSmallerKey(rootNode, num):
    result = -1

    while (rootNode != null):
        if (rootNode.key < num):
            result = rootNode.key
            rootNode = rootNode.right
        else:
            rootNode = rootNode.left

    return result
