import matplotlib.pyplot as plt
import csv

def estimate(t0, t1, a):
    return (t0 + (t1 * a))

def gettheta():
    try:
        with open("theta.txt") as file:
            data = file.read()
            words = data.split()
        theta = [float(words[0]), float(words[1])]
    except:
        theta = [0, 0]
    return (theta)

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

def display(theta, dataset):
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

if __name__ == '__main__':
    theta = gettheta()
    if (theta[0] != 0 or theta[1] != 0):
        dataset = getdataset()
        display(theta, dataset)
    else:
        print("You have not trained you model yet.")