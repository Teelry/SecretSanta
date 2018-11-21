#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:09:58 2018

@author: teelry
How it works:
    

"""
import random

def init(L):
    for i in range(len(L)):
        L[i] = (L[i],None)

def randomizelist(L):
    lgth = len(L)
    for i in range(lgth):
        j = random.randint(0, lgth - 1)
        L[i], L[j] = L[j], L[i]

def givereceive(L):
    for i in range(len(L)):
        L[i] = (L[i][0],L[i-1][0])
            
def printresult(L):
    for person in L:
        print(person[0] + " => " + person[1] + "\n")
        
def secretsanta():
    io = input("Type your friends' names, separated by 1 space (Don't forget your name)\n")
    name = ""
    L = []
    for c in io:
        if c == ' ':
            L.append(name)
            name = ""
        else:
            name += c
    init(L)
    randomizelist(L)
    givereceive(L)
    print("\n")
    printresult(L)
    