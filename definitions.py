import numpy as np
import math


def dis(v1, v2):
    """
    calculate the distance between v1 and v2
    :param v1: a list
    :param v2: a list
    :return:
    """

    v1 = np.array(v1)
    v2 = np.array(v2)

    return math.sqrt((v1 - v2) @ (v1 - v2))


class Family(object):
    """
    class Family has two attributes: center and data item list
    """

    def __init__(self, center):

        self.center = center
        self.data = []

    def means(self):
        """
        :return: the means of current data list
        """

        dataMatrix = []

        for item in self.data:

            dataMatrix.append(item.dataVector)

        colNum = len(dataMatrix[0])
        result = []

        for i in range(colNum):
            result.append(np.average(np.array(dataMatrix)[:, i]))

        return result

    def updateCenter(self):

        newCenter = self.means()

        # the center has changed
        if dis(self.center, newCenter) > 1e-9:
            self.center = newCenter
            return True
        else:
            return False


class Item(object):
    """
    class Item has two attributes: dataVector and the min distance between itself and its family center
    """

    def __init__(self, dataVector):
        self.dataVector = dataVector
        self.minDis = 0
