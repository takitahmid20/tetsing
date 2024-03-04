def knapsack(w, wt, val, n):
    if n == 0 or w == 0:
        return 0
    for i in range(0, n):
        if (val[i]/wt[i])>(val[i+1]/wt[i+1]):
            valtemp[i] = val[i]
            wttemp[i]= wt[i]
            val[i] = val[i+1]
            wt[i] = wt[i+1]
            val[i+1] = valtemp[i]
            wt[i+1] = wttemp[i]

weights = [1, 2, 4, 5]
prices = [7, 15, 34, 40]
w = 4
p = len(prices)
print knapsack(W, weights, prices, p)