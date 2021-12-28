# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:24:03 2021

this code is used to accept the entire input as a list and then process the
same.

@author: ishita2894
"""

import sys
import warnings

import numpy as np

warnings.filterwarnings('ignore')
A = []
Op = np.array([])
maxheap = np.array([])
minheap = np.array([])

""" code to splice the input and return the values """


def input_accept(string):
    input_str = string.split(' ')
    return input_str

def heapify_up(A):
    if len(A) <= 0:
        return

    child = len(A) - 1
    parent = int((child - 1) / 2)

    while child > 0:
        if A[child] < A[parent]:
            A[child], A[parent] = A[parent], A[child]
        else:
            break

        child = parent
        parent = int((child - 1) / 2)


def heapify_down(A,i):
    if len(A) == 0:
        return
    """left child"""
    l = 2 * i + 1
    """right child"""
    r = 2 * i + 2

    if i >= len(A) or l >= len(A):
        return

    if l < len(A) and A[l] < A[i]:
        index = l
    else:
        index = i

    if r < len(A) and A[r] < A[index]:
        index = r
    if index != i:
        A[i], A[index] = A[index], A[i]
        heapify_down(A, index)
""" main code starts here """

for s in sys.stdin:
    input_str = s.rstrip()
    input_str1 = input_accept(input_str)
    if len(input_str) == 0:
        break
    if input_str1[0] == 'a' or input_str1[0] == 'A':
        int_num = int(input_str1[1])
        A.append(int_num)
        heapify_up(A)

    elif input_str1[0] == 'e' or input_str1[0] == 'E':
        output = A[0]
        print(output)
        A[0] = A[len(A) - 1]
        if len(A) > 0:
            A.pop()

        heapify_down(A, 0)
