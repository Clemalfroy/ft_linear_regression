import csv
import matplotlib.pyplot as plt

def estimate(t0, t1, a):
    return (t0 + (t1 * a))

def scale(maxX, minX, dataset):
    scaleddata = []
    for data in dataset:
        new = [(data[0] - minX[0]) / (maxX[0] - minX[0]), data[1]]
        scaleddata.append(new)
    return (scaleddata)

def getdataset():
    tabdata = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            new = []
            c = True
            row = row[0].split(",")
            for elem in row:
                if not elem.isdigit():
                    c = False
                else:
                    new.append(int(elem))
            if c == True:
                tabdata.append(new)
    return (tabdata)

if __name__ == '__main__':

    dataset = getdataset()
    maxX = max(dataset)
    minX = min(dataset)
    m = len(dataset)
    learningrate = 1e-7
    theta = [0.5, 0.5]
    minimalize = learningrate * (1.0 / m)
    scaleddata = scale(maxX, minX, dataset)
    for i in range(0, 10000):
        sumT0 = 0.0
        sumT1 = 0.0
        for data in scaleddata:
            cost = estimate(theta[0], theta[1], data[0]) - data[1]
            sumT0 += cost
            sumT1 += cost * data[0]
        tmptheta0 = minimalize * (sumT0 / m)
        tmptheta1 = minimalize * (sumT1 / m)
        theta[0] -= tmptheta0
        theta[1] -= tmptheta1
    nb = input("Enter a mileage: ")
    if (not nb.isnumeric()):
        print('Wrong format!')
        exit(0)
    for data in dataset:
        plt.plot(data[0], data[1], "bo")
    plt.plot([250000, 100], [estimate(theta[0], theta[1], 250000), estimate(theta[0], theta[1], 100)], 'r-')
    print("With:", nb, "km mileage, you can expect a price of: ", estimate(theta[0], theta[1], int(nb)), "dollars.")
    plt.plot(int(nb), estimate(theta[0], theta[1], int(nb)), "go")
    plt.show()
