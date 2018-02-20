import csv

def estimate(t0, t1, a):
    return (t0 + (t1 * a))

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
    m = len(dataset)
    learningrate = 0.1
    theta0 = 0.5
    theta1 = 0.5
    minimalize = learningrate * (1.0 / m)
    for i in range(0, 30):
        sumT0 = 0.0
        sumT1 = 0.0
        for data in dataset:
            cost = estimate(theta0, theta1, data[0]) - data[1]
            sumT0 += cost
            sumT1 += cost * data[0]
        theta0 = minimalize * (sumT0 / m)
        theta1 = minimalize * (sumT1 / m)
    nb = input("Enter a mileage: ")
    if (not nb.isnumeric()):
        print('Wrong format!')
        exit(0)
    print("With:", nb, "mileaage, you can expect a price of: ", estimate(theta0, theta1, int(nb)))