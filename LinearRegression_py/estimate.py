import matplotlib.pyplot as plt
import gradiantDescent as gd

def gettheta():
    try:
        with open("theta.txt") as file:
            data = file.read()
            words = data.split()
        theta = [float(words[0]), float(words[1])]
    except:
        theta = [0, 0]
    return (theta)

def display(theta, dataset):
    nb = input("Enter a mileage: ")
    if (not nb.isnumeric()):
        print('Wrong format!')
        exit(0)
    for data in dataset:
        plt.plot(data[0], data[1], "bo")
    plt.plot([250000, 100], [gd.estimate(theta[0], theta[1], 250000), gd.estimate(theta[0], theta[1], 100)], 'r-')
    print("With:", nb, "km mileage, you can expect a price of: ", gd.estimate(theta[0], theta[1], int(nb)), "dollars.")
    plt.plot(int(nb), gd.estimate(theta[0], theta[1], int(nb)), "go")
    plt.show()

if __name__ == '__main__':
    theta = gettheta()
    if (theta[0] != 0 or theta[1] != 0):
        dataset = gd.getdataset()
        display(theta, dataset)
    else:
        print("You have not trained you model yet.")