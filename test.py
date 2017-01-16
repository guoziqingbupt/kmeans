import readData
import kmeans


def main(fileName, k):

    data = readData.readData(fileName)
    results = kmeans.kmeans(data, k)

    for family in results:

        for item in family.objList:
            print(item)
        print("**********************")


if __name__ == "__main__":
    main("k_meansData.csv", 4)
