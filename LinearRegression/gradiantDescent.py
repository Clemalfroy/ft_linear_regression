def estimate(t0,t1,a):
    return (t0 + t1 * a)

if __name__ == '__main__':
    tab = [[0, 5], [0, 6], [1, 4], [3, 2], [4, 1]]

    alpha = 0.1
    teta0 = 0
    teta1 = 0

    tempteta0 = 0
    tempteta1 = 0

    for i in range(0, 5000):
        sum1 = 0
        sum2 = 0
        for data in tab:
            cost = (teta0 + teta1 * data[0]) - data[1]
            sum1 = sum1 + cost
            sum2 = sum2 + cost * data[0]
        tempteta0 = teta0 - alpha * 1 / (len(tab)) * sum1
        tempteta1 = teta1 - alpha * 1 / (len(tab)) * sum2
        teta0 = tempteta0
        teta1 = tempteta1
    print(teta0)
    print(teta1)
    print(estimate(teta0, teta1, 1))