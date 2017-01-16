import csv


def readData(fileName):

    data = []

    with open(fileName) as csvFile:

        reader = csv.reader(csvFile)

        for item in reader:

            temp = []

            for attribute in item:
                temp.append(float(attribute))

            data.append(temp)

    return data


