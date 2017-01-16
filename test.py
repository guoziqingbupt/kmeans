import readData
import kmeans


def main(fileName, k):

    data = readData.readData(fileName)
    results = kmeans.kmeans(data, k)

    for family in results:

        for item in family.objList:
            print(item)
        print("**********************")


# two datasets, one is small, one is large
if __name__ == "__main__":

    # "k_meansData.csv"
    main("testData.csv", 3)
