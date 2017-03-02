import random
from definitions import *


def cluster(data, families):
    """
    make each data item into each families; assign the distance of the item and its center
    :param data: a list contained data items
    :param families: contains the center and the list of data items
    :return: None
    """

    for item in data:

        # Initialize:
        item.minDis = dis(item.dataVector, families[0].center)
        minIndex = 0
        count = 1

        # find the family for one data item
        for family in families[1:]:

            temp = dis(item.dataVector, family.center)
            if temp < item.minDis:

                # update the item's min distance,
                item.minDis = temp
                minIndex = count
            count += 1

        # add the data item into the family
        families[minIndex].data.append(item)


def kmeans(sourceData, k):
    """

    :param sourceData: 2-dimension array
    :param k:
    :return:families
    """

    # generate data item list
    data = []
    for i in sourceData:
        data.append(Item(i))

    # give the initial families, or make centers = random.sample(sourceData, k)
    centers = ([2, 10], [5, 8], [1, 2])
    families = [Family(center) for center in centers]

    # Next: execute the next iteration or not
    Next = True

    while Next:

        # clear the family's data item list
        for family in families:
            family.data.clear()

        # cluster
        cluster(data, families)
        Next = False

        for family in families:
            if family.updateCenter():
                Next = True
    return families


def genCenters(data, k):
    """
    generate initialized centers
    :param data: a list contained data items
    :param k:
    :return: families
    """

    # initialize one center and corresponding families.
    # Note that random.sample(data, 1) is a list that have one element.
    c1 = random.sample(data, 1)[0]
    families = [Family(c1.dataVector)]

    # generate other k - 1 centers and corresponding families
    for i in range(k - 1):

        cluster(data, families)
        sumDis = sum([item.minDis for item in data])
        candidate = None

        # Random is a random number less than sumDis
        Random = random.uniform(0, sumDis)

        # tempList stores the candidate that has been chosen
        tempList = []

        while Random > 0:
            candidate = random.sample(data, 1)[0]
            while candidate in tempList:
                candidate = random.sample(data, 1)[0]
            tempList.append(candidate)
            Random -= candidate.minDis

        families.append(Family(candidate.dataVector))

    return families


def kmeansPlusPlus(sourceData, k):

    data = []
    for i in sourceData:
        data.append(Item(i))

    families = genCenters(data, k)

    Next = True
    while Next:

        for family in families:
            family.data.clear()

        cluster(data, families)
        Next = False

        for family in families:
            if family.updateCenter():
                Next = True
    return families
