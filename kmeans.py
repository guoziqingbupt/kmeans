import random
import numpy as np


class Family(object):
    """docstring for Family"""
    def __init__(self, center):

        self.center = center
        self.objList = []

    def addObj(self, obj):

        self.objList.append(obj)

    def reGetCenter(self):

        self.center = sum(np.array(self.objList)[:]) / len(self.objList)


def setup(data, families):
    """
    Assigning the data items into families for the first time
    :param data: source data
    :param families: the families generated in initialization
    :return: None
    """

    # Finding the family that the data item with min distance
    for item in data:
    
        # initializing the min distance and
        min_dis = distance(item, families[0].center)
        min_family = families[0]
        
        for family in families:
            tempDis = distance(item, family.center)

            if tempDis < min_dis:
                min_dis = tempDis
                min_family = family

        min_family.addObj(item)


def helper(data, families, Next):
    """
    iteration function
    :param data:
    :param families:
    :param Next: determining whether to execute the next iteration or not
    :return:
    """

    for item in data:

        min_dis = distance(item, families[0].center)
        min_family = families[0]
        tempFamily = None

        for family in families:

            if item in family.objList:
                tempFamily = family

            tempDis = distance(item, family.center)

            if tempDis < min_dis:

                min_dis = tempDis
                min_family = family

        if item not in min_family.objList:

            min_family.objList.append(item)
            tempFamily.objList.remove(item)
            Next = True

    return Next


def kmeans(data, k):

    kcenters = random.sample(data, k)
    families = []

    # constructing families
    for center in kcenters:

        families.append(Family(center))

    Next = True

    setup(data, families)

    while Next:

        Next = False
        Next = helper(data, families, Next)

        for family in families:
            family.reGetCenter()

    return families


def distance(obj1, obj2):

    diff = np.array(obj1) - np.array(obj2)

    return diff @ diff
