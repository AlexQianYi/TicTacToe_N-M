#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:22:31 2018

@author: yiqian
"""

from Board import Board, X, O, Empty
from MiniMax import Node, minMax, AlphaBeta

n = 15
m = 5

def play():
    global m, n

    """
    print('input n')
    n = int(input())
    print('input m')
    m = int(input())
    """
    n = 15
    m = 5
    board = Board(n, n, m)
    board.display()
    
    side = True
    print('please choose side: x or o')
    choose = input()
    if choose=='x':
        side = True
    else:
        side = False
        
    status = X
    deep = 2
    while True:
        
        if side:
            print('your turn ' + str(status) + 'input x and y')
            x = int(input())
            y = int(input())
            side = not side
        else:
            node = Node(board, deep, status)
            print('wait AI...')
            score = AlphaBeta(node)
            print('AI done')
            x, y = node.Pos_i, node.Pos_j
            print(x, y, status)
            side = not side
        
        
        board.move(x, y, status)
        
        board.display()
        
        if board.check(x, y, status):
            if status == X:
                print ('X win!')
            else:
                print ('O win!')
            break
        elif board.is_full():
            print ('draw game!')
        else:
            status = X^status^O

if __name__=='__main__':
    play()