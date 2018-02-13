def estimate(t0, t1, a):
    return (t0 + (t1 * a))

if __name__ == '__main__':
    tabdata = [[0, 5], [0, 6], [1, 4], [3, 2], [4, 1]]
    m = len(tabdata)
    alpha = 0.2
    teta0 = 0
    teta1 = 0
    for i in range(0, m * 100):
        sum1 = 0
        sum2 = 0
        for data in tabdata:
            cost = (teta0 + teta1 * data[0]) - data[1]
            sum1 = sum1 + cost
            sum2 = sum2 + cost * data[0]
        minimalize = alpha * 1 / m
        teta0 -= minimalize * sum1
        teta1 -= minimalize * sum2
    nb = int(input("Entrez un nombre a estimer: "))
    print(estimate(teta0, teta1, nb))