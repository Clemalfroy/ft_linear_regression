import csv

def estimate(t0, t1, a):
    return (t0 + (t1 * a))

def scale(maxX, minX, dataset):
    scaleddata = []
    for data in dataset:
        new = [(data[0] / (maxX[0] - minX[0])), data[1]]
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
    learningrate = 0.1
    theta = [0, 0]
    minimalize = learningrate * (1.0 / m)
    scaleddata = scale(maxX, minX, dataset)
    costfunction = 0
    previouscost = -999999
    while (abs(costfunction - previouscost) > 0.0003):
        previouscost = costfunction
        sumT0 = 0.0
        sumT1 = 0.0
        for data in scaleddata:
            cost = estimate(theta[0], theta[1], data[0]) - data[1]
            sumT0 += cost
            sumT1 += cost * data[0]
        theta[0] = theta[0] - learningrate * (1 / m) * (sumT0 / m)
        theta[1] = theta[1] - learningrate * (1 / m) * (sumT1 / m)
        costfunction = 1 / m  * pow(sumT0, 2)
    theta[1] = (theta[1] / (maxX[0] - minX[0]))
    print("theta0: ", theta[0], " |||||| theta1: ", theta[1])
    f = open("theta.txt", "w")
    lines_of_text = [str(theta[0]), "\n", str(theta[1]),  "\n"]
    f.writelines(lines_of_text)
    f.close()
