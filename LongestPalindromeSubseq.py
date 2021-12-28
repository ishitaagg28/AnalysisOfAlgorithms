# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:14:46 2021

@author: ishita2894
"""

def list2Str(s):
    string = ""
    for i in s:
        string += i
    return string


def longestPalindrome(string):
    m = len(string)
    rev = string[::-1]
    n = len(rev)
    o = m+1
    p = n+1
    
    arr = [[0 for i in range(o)]for j in range(p)]
    for i in range(o):
        for j in range(p):
            if i == 0 or j ==0:
                arr[i][j] = 0
            elif string[i-1] == rev[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    
    var = arr[m][n]
    
    
    a = ["\n"]*(var+1)
    x = m
    y = n
    
    while x > 0 and j > 0:
        if string[i-1] == rev[j-1]:
            a[var-1] = string[i-1]
            i = i-1
            j = j-1
            var = var-1
        elif arr[i-1][j] > arr[i][j-1]:
            i = i-1
        else:
            j = j-1
            
    return a[:-1]


s = input()
op = list2Str(longestPalindrome(s))
print(len(op))
print(op)
