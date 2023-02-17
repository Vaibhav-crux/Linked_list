# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:57:22 2022

@author: Vaibhav Tiwari
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def print_LL(self):
        if(self.head is None):
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
                
LL1=LinkedList()

LL1.print_LL()


            