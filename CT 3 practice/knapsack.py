def knapsack(n, weight, profit, capacity):
    
    total_profit = 0
    selected_items = []
    u = capacity
    while u > 0:
        max_index = -1
        max_ratio = -1
        for i in range(n):
            if weight[i] > 0 and weight[i] <= u and profit[i] / weight[i]>max_ratio:
                max_ratio = profit[i]/weight[i]
                max_index = i
            
        if max_index == -1:
            break

        selected_items.append(max_ratio)
        total_profit = total_profit+profit[max_index]
        u = u-weight[max_index]
        weight[max_index] = 0
    
    print("selected items: ", selected_items)
    print(total_profit)


    # for i in range(n):
    #     for j in range(i+1, n):
    #         if profit[i]<profit[j]:
    #             temp = profit[i]
    #             profit[i]=profit[j]
    #             profit[j]=temp
            
    #         if weight[i]<weight[j]:
    #             temp = weight[i]
    #             weight[i]=weight[j]
    #             weight[j]=temp

    # print(profit)
    # print(weight)



weight = [3, 5, 6, 12, 14, 1]
profit = [25, 32, 33, 55, 65, 40]

#per kg = 25/3 = 8.333
# 32/5 = 6.4
capacity = 20
#temp = None
ratio = []
n = len(weight)
for i in range(n):
    ratio.append(profit[i] / weight[i])

for i in range(n):
    for j in range(i+1,n): # 0+1
        if ratio[i]<ratio[j]: # if ratio[0]<ratio[1]
            temp = ratio[j]
            ratio[j]=ratio[i]
            ratio[i] = temp
                                    # weight = [3, 5, 6, 12, 14, 1]
                                    # profit = [25, 32, 33, 55, 65, 40]
            temp = weight[j]
            weight[j]=weight[i]
            weight[i]=temp

            temp=profit[j]
            profit[j]= profit[i]
            profit[i]=temp

knapsack(n, weight, profit, capacity)
    