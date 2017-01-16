import random
import numpy as np


class Family(object):

    def __init__(self, center):

        self.center = center
        self.objList = []

    def addObj(self, obj):

        # add objects to family
        self.objList.append(obj)

    def reGetCenter(self):

        # get means
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

    # select k centers randomly
    kcenters = random.sample(data, k)

    # constructing families
    families = []
    for center in kcenters:

        families.append(Family(center))

    # Next: whether to execute or not
    Next = True
    setup(data, families)

    while Next:

        Next = False

        for family in families:
            family.reGetCenter()

        Next = helper(data, families, Next)

    return families


def distance(obj1, obj2):

    diff = np.array(obj1) - np.array(obj2)

    return diff @ diff
