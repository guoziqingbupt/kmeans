import readData
from kmeans import *


def main(fileName, k):

    sourceData = readData.readData(fileName)

    result1 = kmeans(sourceData, k)
    result2 = kmeansPlusPlus(sourceData, k)

    return result1, result2


if __name__ == "__main__":

    result = main("testData.csv", 3)

    r1, r2 = result[0], result[1]

    for family in r1:
        for item in family.data:
            print(item.dataVector, ", ")
        print("***************")

    print("------------------------")

    for family in r2:
        for item in family.data:
            print(item.dataVector, ", ")
        print("***************")
