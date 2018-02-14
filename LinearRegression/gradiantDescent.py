import csv

def estimate(t0, t1, a):
    return (t0 + (t1 * a))

def readdata():
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

    tabdata = readdata()
    m = len(tabdata)
    learningrate = 1e-10
    teta0 = 0
    teta1 = 0
    for i in range(0, 5100):
        sum1 = 0
        sum2 = 0
        print (teta0)
        for data in tabdata:
            cost = (teta0 + teta1 * data[0]) - data[1]
            sum1 = sum1 + cost
            sum2 = sum2 + cost * data[0]
        minimalize = learningrate * 1 / m
        teta0 -= minimalize * sum1
        teta1 -= minimalize * sum2
    nb = int(input("Entrez un nombre a estimer: "))
    print(teta0)
    print(teta1)
    print(estimate(teta0, teta1, nb))