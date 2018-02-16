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
    learningrate = 1e-6
    teta0 = 0.0
    teta1 = 0.0
    minimalize = learningrate * (1.0 / m)
    for i in range(0, 30):
        sumT0 = 0.0
        sumT1 = 0.0
        print("teta0: ", teta0, "       teta1: ", teta1)
        for data in dataset:
            cost = estimate(teta0, teta1, data[0]) - data[1]
            sumT0 += cost
            sumT1 += cost * data[0]
        teta0 = minimalize * (sumT0 / m)
        teta1 = minimalize * (sumT1 / m)
    nb = input("Enter a mileage: ")
    if (not nb.isnumeric()):
        print('Wrong format!')
        exit(0)
    print(estimate(teta0, teta1, int(nb)))