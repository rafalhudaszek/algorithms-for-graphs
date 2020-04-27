import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random

#check if string is a graphic string
def isGraphic(listOfNumbers, lenOfList):
    listOfNumbers.sort(reverse = True)
    while True:
        if all([True if i == 0 in listOfNumbers else False for i in listOfNumbers]): 
            return True
        elif (listOfNumbers[0] >= lenOfList) or any([True if i<0 in listOfNumbers else False for i in listOfNumbers]):
            return False
        for i  in range(listOfNumbers[0] + 1):
            listOfNumbers[i] = listOfNumbers[i] - 1
        listOfNumbers[0] = 0
        listOfNumbers.sort(reverse = True)

#returns neighborhood_list from graphic string
def listFromGraphic(listOfNumbers):
    listOfNumbers.sort(reverse = True)
    #tworzenie listy dwuwymiarowej
    tabTab = [None] * len(listOfNumbers)
    for i in range(0,len(listOfNumbers)):
        tabTab[i] = [] 

    for i in tabTab:
        val = tabTab.index(i) + 1
        while listOfNumbers[tabTab.index(i)] > 0:
            if listOfNumbers[val] > 0:
                i.append(val)
                tabTab[val].append(tabTab.index(i))
                listOfNumbers[tabTab.index(i)] = listOfNumbers[tabTab.index(i)] - 1
                listOfNumbers[val] = listOfNumbers[val] - 1

            val = val + 1
    string = ''
    iterator = 1
    for i in tabTab:
        string = string + str(iterator) + '.'
        for j in i:
            string = string + ' ' + str(j) 
        string += '\n'
        iterator += 1
    return string
